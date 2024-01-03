#!/usr/bin/env ruby
#
# Checking if argument is provided
if ARGV.empty?
  puts "Usage: ruby match_patterns.rb <input>"
else
  # Obtains the argument
  input = ARGV[0]

  # defining the pattern
  pattern = /h(.{2,})n/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts input
  else
    puts ""
  end
end
