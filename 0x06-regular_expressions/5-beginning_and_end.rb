#!/usr/bin/env ruby
#
# Checking if argument exists
if ARGV.empty?
  puts "Usage: ruby match_patterns.rb <input>"
else
  # Obtaining the argument
  input = ARGV[0]

  #definng the pattern
  pattern =  /^h.n$/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts input
  else
    puts ""
  end
end
