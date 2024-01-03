#!/usr/bin/env ruby
#
# Checking for provided argument
if ARGV.empty?
  puts "Usage: ruby simple_script.rb <input>"
else
  # Obtaining the argument
  input = ARGV[0]

  # Defing the pattern
  pattern = /hb(t{2,5})n/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts input
  else
    puts ""
  end
end
