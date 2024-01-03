#!/usr/bin/env ruby
#
# Checks if argument exists
if ARGV.empty?
  puts "Usage: ruby match_patterns.rb <input>"
else
  # Obtain the argument
  input = ARGV[0]

  # Define the pattern
  pattern = /[A-Z]/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts matches.join
  else
    puts ""
  end
end
