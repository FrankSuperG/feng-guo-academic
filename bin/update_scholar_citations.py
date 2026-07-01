#!/usr/bin/env python

import os
import re
import sys
import yaml
import html
import signal
import socket
import urllib.request
from contextlib import contextmanager
from datetime import datetime


def env_int(name: str, default: int) -> int:
    """Read a positive integer environment setting."""
    try:
        value = int(os.environ.get(name, str(default)))
        return value if value > 0 else default
    except ValueError:
        return default


NETWORK_TIMEOUT_SECONDS = env_int("CITATION_NETWORK_TIMEOUT", 20)
SCHOLARLY_FALLBACK_TIMEOUT_SECONDS = env_int("SCHOLARLY_FALLBACK_TIMEOUT", 120)
USE_SCHOLARLY_FALLBACK = os.environ.get("USE_SCHOLARLY_FALLBACK", "").lower() in {
    "1",
    "true",
    "yes",
}

socket.setdefaulttimeout(NETWORK_TIMEOUT_SECONDS)


class CitationUpdateTimeout(TimeoutError):
    """Raised when a citation update stage exceeds its local deadline."""


@contextmanager
def time_limit(seconds: int, label: str):
    """Limit slow fallback calls so scheduled workflows do not hang indefinitely."""
    if not hasattr(signal, "SIGALRM"):
        yield
        return

    previous_handler = signal.getsignal(signal.SIGALRM)

    def handle_timeout(_signum, _frame):
        raise CitationUpdateTimeout(f"{label} exceeded {seconds} seconds")

    signal.signal(signal.SIGALRM, handle_timeout)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous_handler)


def load_scholar_user_id() -> str:
    """Load the Google Scholar user ID from the configuration file."""
    config_file = "_data/socials.yml"
    if not os.path.exists(config_file):
        print(
            f"Configuration file {config_file} not found. Please ensure the file exists and contains your Google Scholar user ID."
        )
        sys.exit(1)
    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
        scholar_user_id = config.get("scholar_userid")
        if not scholar_user_id:
            print(
                "No 'scholar_userid' found in the configuration file. Please add 'scholar_userid' to _data/socials.yml."
            )
            sys.exit(1)
        return scholar_user_id
    except yaml.YAMLError as e:
        print(
            f"Error parsing YAML file {config_file}: {e}. Please check the file for correct YAML syntax."
        )
        sys.exit(1)


SCHOLAR_USER_ID: str = load_scholar_user_id()
OUTPUT_FILE: str = "_data/citations.yml"


def clean_html_text(raw_text: str) -> str:
    """Convert a small HTML fragment to plain text."""
    text = re.sub(r"<[^>]+>", "", raw_text)
    text = html.unescape(text)
    text = re.sub(r"[\u202a-\u202e]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_int(raw_value: str) -> int:
    """Parse Google Scholar integer fields that may contain commas or blanks."""
    value = clean_html_text(raw_value).replace(",", "")
    return int(value) if value else 0


def empty_citation_data(today: str) -> dict:
    """Create the citation data structure written to _data/citations.yml."""
    return {
        "metadata": {
            "last_updated": today,
            "source": f"Google Scholar profile {SCHOLAR_USER_ID}",
        },
        "profile": {},
        "papers": {},
    }


def get_profile_html() -> str:
    """Fetch the public Google Scholar profile page."""
    url = (
        "https://scholar.google.com/citations"
        f"?user={SCHOLAR_USER_ID}&hl=en&pagesize=100"
    )
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=NETWORK_TIMEOUT_SECONDS) as response:
        return response.read().decode("utf-8", errors="replace")


def get_public_profile_citations(today: str) -> dict:
    """Fetch citation data from the public Google Scholar profile HTML."""
    profile_html = get_profile_html()
    citation_data = {
        "metadata": {
            "last_updated": today,
            "source": f"Google Scholar profile {SCHOLAR_USER_ID}",
        },
        "profile": {},
        "papers": {},
    }

    stat_values = re.findall(r'class="gsc_rsb_std">([^<]*)</td>', profile_html)
    if len(stat_values) < 6:
        raise ValueError("Could not find the Google Scholar citation summary table.")

    citation_data["profile"] = {
        "citations": parse_int(stat_values[0]),
        "citations_since_2021": parse_int(stat_values[1]),
        "h_index": parse_int(stat_values[2]),
        "h_index_since_2021": parse_int(stat_values[3]),
        "i10_index": parse_int(stat_values[4]),
        "i10_index_since_2021": parse_int(stat_values[5]),
    }

    rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', profile_html, re.DOTALL)
    if not rows:
        raise ValueError("Could not find publication rows on the Google Scholar profile.")

    for row in rows:
        id_match = re.search(
            rf"citation_for_view={re.escape(SCHOLAR_USER_ID)}:([^\"&]+)", row
        )
        title_match = re.search(
            r'class="gsc_a_at"[^>]*>(.*?)</a>', row, re.DOTALL
        )
        year_match = re.search(
            r'class="gsc_a_h gsc_a_hc gs_ibl">([^<]*)</span>', row
        )
        citation_match = re.search(
            r'class="gsc_a_ac[^"]*"[^>]*>(.*?)</a>', row, re.DOTALL
        )
        if not id_match or not title_match:
            continue

        pub_id = f"{SCHOLAR_USER_ID}:{html.unescape(id_match.group(1))}"
        title = clean_html_text(title_match.group(1))
        year = clean_html_text(year_match.group(1)) if year_match else "Unknown Year"
        citations = parse_int(citation_match.group(1)) if citation_match else 0

        print(f"Found: {title} ({year}) - Citations: {citations}")
        citation_data["papers"][pub_id] = {
            "title": title,
            "year": year,
            "citations": citations,
        }

    return citation_data


def get_scholarly_citations(today: str) -> dict:
    """Fetch citation data through the scholarly package as a fallback."""
    try:
        from scholarly import scholarly
    except ImportError:
        raise RuntimeError(
            "The scholarly package is not installed and the public profile fallback failed."
        )

    citation_data = empty_citation_data(today)
    scholarly.set_timeout(10)
    scholarly.set_retries(1)
    try:
        author = scholarly.search_author_id(SCHOLAR_USER_ID)
        author_data = scholarly.fill(author)
    except Exception as e:
        raise RuntimeError(
            f"Error fetching author data from Google Scholar for user ID '{SCHOLAR_USER_ID}': {e}. Please check your internet connection and Scholar user ID."
        ) from e

    if not author_data:
        raise RuntimeError(
            f"Could not fetch author data for user ID '{SCHOLAR_USER_ID}'. Please verify the Scholar user ID and try again."
        )

    if "publications" not in author_data:
        raise RuntimeError(
            f"No publications found in author data for user ID '{SCHOLAR_USER_ID}'."
        )

    citation_data["profile"] = {
        "citations": author_data.get("citedby", 0),
        "citations_since_2021": author_data.get("citedby5y", 0),
        "h_index": author_data.get("hindex", 0),
        "h_index_since_2021": author_data.get("hindex5y", 0),
        "i10_index": author_data.get("i10index", 0),
        "i10_index_since_2021": author_data.get("i10index5y", 0),
    }
    print(
        "Profile metrics: "
        f"{citation_data['profile']['citations']} citations, "
        f"h-index {citation_data['profile']['h_index']}, "
        f"i10-index {citation_data['profile']['i10_index']}"
    )

    for pub in author_data["publications"]:
        try:
            pub_id = pub.get("pub_id") or pub.get("author_pub_id")
            if not pub_id:
                print(
                    f"Warning: No ID found for publication: {pub.get('bib', {}).get('title', 'Unknown')}. This publication will be skipped."
                )
                continue

            title = pub.get("bib", {}).get("title", "Unknown Title")
            year = pub.get("bib", {}).get("pub_year", "Unknown Year")
            citations = pub.get("num_citations", 0)

            print(f"Found: {title} ({year}) - Citations: {citations}")

            citation_data["papers"][pub_id] = {
                "title": title,
                "year": year,
                "citations": citations,
            }
        except Exception as e:
            print(
                f"Error processing publication '{pub.get('bib', {}).get('title', 'Unknown')}': {e}. This publication will be skipped."
            )

    return citation_data


def get_scholar_citations() -> None:
    """Fetch and update Google Scholar citation data."""
    print(f"Fetching citations for Google Scholar ID: {SCHOLAR_USER_ID}")
    today = datetime.now().strftime("%Y-%m-%d")
    existing_data = None

    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r") as f:
                existing_data = yaml.safe_load(f)
            if (
                existing_data
                and "metadata" in existing_data
                and "last_updated" in existing_data["metadata"]
            ):
                print(f"Last updated on: {existing_data['metadata']['last_updated']}")
        except Exception as e:
            print(
                f"Warning: Could not read existing citation data from {OUTPUT_FILE}: {e}. The file may be missing or corrupted."
            )

    try:
        citation_data = get_public_profile_citations(today)
        print("Citation data fetched from the public Google Scholar profile page.")
    except Exception as public_profile_error:
        print(f"Public profile fetch failed: {public_profile_error}")
        if USE_SCHOLARLY_FALLBACK:
            print(
                f"Falling back to the scholarly package with a {SCHOLARLY_FALLBACK_TIMEOUT_SECONDS}-second deadline."
            )
            try:
                with time_limit(
                    SCHOLARLY_FALLBACK_TIMEOUT_SECONDS, "scholarly fallback"
                ):
                    citation_data = get_scholarly_citations(today)
            except Exception as scholarly_error:
                print(f"Scholarly fallback failed: {scholarly_error}")
                if existing_data:
                    print("Keeping existing citation data unchanged.")
                    return
                sys.exit(1)
        elif existing_data:
            print(
                "Keeping existing citation data unchanged. Set USE_SCHOLARLY_FALLBACK=1 to allow the slower scholarly fallback."
            )
            return
        else:
            print(
                "No existing citation data is available, so the citation update cannot continue."
            )
            sys.exit(1)

    if (
        existing_data
        and existing_data.get("profile") == citation_data["profile"]
        and existing_data.get("papers") == citation_data["papers"]
    ):
        print("No changes in citation data. Skipping file update.")
        return

    try:
        with open(OUTPUT_FILE, "w") as f:
            yaml.safe_dump(citation_data, f, width=1000, sort_keys=False)
        print(f"Citation data saved to {OUTPUT_FILE}")
    except Exception as e:
        print(
            f"Error writing citation data to {OUTPUT_FILE}: {e}. Please check file permissions and disk space."
        )
        sys.exit(1)


if __name__ == "__main__":
    try:
        get_scholar_citations()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
