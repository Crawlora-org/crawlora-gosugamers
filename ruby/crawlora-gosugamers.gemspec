require_relative "lib/crawlora/gosugamers/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-gosugamers"
  spec.version = Crawlora::Gosugamers::VERSION
  spec.summary = "GosuGamers API client for Crawlora (17 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted GosuGamers API. Covers esports matches, results, tournaments, games, news, and articles across 17 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-gosugamers", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
