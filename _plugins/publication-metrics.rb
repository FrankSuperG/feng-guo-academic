require 'bibtex'

module Jekyll
  class PublicationMetricsGenerator < Generator
    priority :low

    def generate(site)
      scholar = site.config.fetch('scholar', {})
      source = scholar.fetch('source', '_bibliography').sub(%r{\A/+}, '')
      path = File.join(site.source, source, scholar.fetch('bibliography', 'papers.bib'))
      bibliography = BibTeX.open(path)
      unless bibliography.errors.empty?
        raise "Cannot calculate publication metrics: invalid bibliography #{path}"
      end

      papers = bibliography.entries.values.select do |entry|
        %w[article inproceedings].include?(entry.type.to_s) &&
          entry[:pubstate].to_s != 'presentation'
      end

      site.data['publication_metrics'] = {
        'published_accepted' => papers.count do |entry|
          %w[published accepted].include?(entry[:pubstate].to_s)
        end,
        'preprints' => papers.count do |entry|
          %i[arxiv ssrn].any? { |field| !entry[field].to_s.strip.empty? }
        end
      }
    end
  end
end
