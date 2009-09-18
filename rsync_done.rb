#!/usr/bin/env ruby
def rsync_running?
  pid = `pgrep rsync`.chomp
  return !pid.empty?
end

def test
  if !rsync_running?
    puts "rsync is done!" 
    system('mpc play')
  else
    puts "."
    sleep(5)
    test
  end
end

puts "Running til rsync finishes!"
test
