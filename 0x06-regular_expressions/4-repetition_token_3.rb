#!/usr/bin/env ruby
#
# Checks for arguments
if ARGV.empty?
  puts "Usage: ruby match_patterns.rb <input>"
else
  # Obtain the argument
  input = ARGV[0]

  # Define the pattern
  pattern = /^(?!hbo)/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts input
  else
    puts ""
  end
end
