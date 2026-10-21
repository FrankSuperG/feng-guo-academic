require 'minitest/autorun'
require 'tmpdir'
require 'fileutils'
require 'set'
require 'jekyll/plugin'
require 'jekyll/generator'
require_relative '../_plugins/publication-metrics'

class PublicationMetricsTest < Minitest::Test
  def metrics(content)
    Dir.mktmpdir do |source|
      FileUtils.mkdir_p(File.join(source, 'references'))
      File.write(File.join(source, 'references', 'works.bib'), content)
      site = Struct.new(:source, :config, :data).new(
        source,
        { 'scholar' => { 'source' => '/references/', 'bibliography' => 'works.bib' } },
        {}
      )
      Jekyll::PublicationMetricsGenerator.new.generate(site)
      site.data.fetch('publication_metrics')
    end
  end

  def test_published_and_accepted_papers_both_count
    result = metrics(<<~BIB)
      @article{published, pubstate = {published}}
      @inproceedings{accepted, pubstate = {accepted}}
      @article{preprint, pubstate = {preprint}, arxiv = {2601.00001}}
    BIB
    assert_equal 2, result['published_accepted']
    assert_equal 1, result['preprints']
  end

  def test_multiple_preprint_links_count_as_one_paper
    result = metrics(<<~BIB)
      @article{both, pubstate = {published}, arxiv = {2601.00001}, ssrn = {https://ssrn.com/abstract=1}}
      @article{ssrn, pubstate = {preprint}, ssrn = {https://ssrn.com/abstract=2}}
      @article{empty, pubstate = {published}, arxiv = {}, ssrn = { }}
    BIB
    assert_equal 2, result['preprints']
  end

  def test_talks_and_datasets_are_not_papers
    result = metrics(<<~BIB)
      @inproceedings{talk, pubstate = {presentation}, arxiv = {2601.00001}}
      @misc{dataset, pubstate = {published}, ssrn = {https://example.com}}
    BIB
    assert_equal 0, result['published_accepted']
    assert_equal 0, result['preprints']
    assert_empty result['by_year']
  end

  def test_new_papers_and_publication_status_changes_are_recalculated
    preprint = '@article{one, pubstate = {preprint}, arxiv = {2601.00001}}'
    assert_equal 0, metrics(preprint)['published_accepted']
    published = preprint.sub('{preprint}', '{published}')
    result = metrics(published + "\n@article{two, pubstate = {accepted}}")
    assert_equal 2, result['published_accepted']
    assert_equal 1, result['preprints']
  end

  def test_empty_bibliography_has_zero_metrics
    result = metrics('')
    assert_equal 0, result['published_accepted']
    assert_equal 0, result['preprints']
    assert_empty result['by_year']
    assert_equal 1, result['maximum_year_count']
  end

  def test_bibliography_with_jekyll_front_matter
    result = metrics("---\n---\n@article{one, pubstate = {published}}")
    assert_equal 1, result['published_accepted']
  end

  def test_yearly_chart_fills_gaps_and_excludes_preprints_and_talks
    result = metrics(<<~BIB)
      @article{first, pubstate = {published}, year = {2024}}
      @article{second, pubstate = {accepted}, year = {2026}}
      @inproceedings{third, pubstate = {published}, year = {2026}}
      @article{preprint, pubstate = {preprint}, year = {2025}, arxiv = {2501.00001}}
      @inproceedings{talk, pubstate = {presentation}, year = {2025}}
    BIB
    assert_equal [
      { 'year' => 2024, 'count' => 1, 'cumulative' => 1 },
      { 'year' => 2025, 'count' => 0, 'cumulative' => 1 },
      { 'year' => 2026, 'count' => 2, 'cumulative' => 3 }
    ], result['by_year']
    assert_equal 2, result['maximum_year_count']
    assert_equal result['published_accepted'], result['by_year'].last['cumulative']
  end
end
