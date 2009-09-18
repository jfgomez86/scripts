#!/usr/bin/env ruby
def pacman_running?
  pid = `pgrep pacman`.chomp
  return !pid.empty?
end

def shutdown
  if !pacman_running?
    puts "Shutting down in 3 minutes!" 
    `sudo shutdown -h +3` if !pacman_running?
  else
    puts "pacman still running. Can't shutdown."
    sleep(5)
    shutdown
  end
end

shutdown
