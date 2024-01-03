#!/usr/bin/env ruby
#
# Checking for arguments
if ARGV.empty?
  puts "Usage: ruby match_patterns.rb <input>"
else
  # obtaining the argument
  input = ARGV[0]

  # defining the pattern
  pattern = /h(.{1,2})n/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts input
  else
    puts ""
  end
end
