require 'net/http'
require 'uri'
require 'json'

def post_request(url, body_params)
  uri = URI.parse(url)

  if uri.scheme == 'https'
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true 
  else
    http = Net::HTTP.new(uri.host, uri.port)
  end

  request = Net::HTTP::Post.new(uri.path, { 'Content-Type' => 'application/json' })
  request.body = body_params.to_json

  response = http.request(request)
  puts "Response status: #{response.code} #{response.message}" 
  puts "Response body:\n#{response.body}"
end
