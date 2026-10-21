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

      published = papers.select { |entry| %w[published accepted].include?(entry[:pubstate].to_s) }
      years = published.map { |entry| entry[:year].to_s }.select { |year| year.match?(/\A\d{4}\z/) }.map(&:to_i)
      cumulative = 0
      by_year = years.empty? ? [] : (years.min..years.max).map do |year|
        count = published.count { |entry| entry[:year].to_s == year.to_s }
        cumulative += count
        { 'year' => year, 'count' => count, 'cumulative' => cumulative }
      end

      site.data['publication_metrics'] = {
        'published_accepted' => published.size,
        'preprints' => papers.count do |entry|
          %i[arxiv ssrn].any? { |field| !entry[field].to_s.strip.empty? }
        end,
        'by_year' => by_year,
        'maximum_year_count' => [by_year.map { |row| row['count'] }.max.to_i, 1].max
      }
    end
  end
end
