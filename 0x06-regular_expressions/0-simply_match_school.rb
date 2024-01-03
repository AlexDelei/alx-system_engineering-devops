#!/usr/bin/env ruby
#
#Checking for argument
if ARGV.empty?
  puts "Usage: ruby simple_script.rb <input>"

else
  # Getting the argument from the command line
  input = ARGV[0]

  # Defining the pattern
  pattern = /(?=(School))/

  matches = input.scan(pattern).flatten

  if matches.any?
    puts matches.join
  else
    puts ""
  end
end
