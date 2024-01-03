#!/usr/bin/env ruby
#
# Checking if any argument was provided
if ARGV.empty?
  puts "Usage: ruby match_patterns.rb <input>"
else
  # Obtaining the argument
  input = ARGV[0]

  # defining the pattern
  pattern = /^\d{10}$/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts input
  else
    puts ""
  end
end
