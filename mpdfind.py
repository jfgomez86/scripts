#!/usr/bin/env python

import commands
import gobject
from gui import *
import re
 
class Pympdfind:
   def __init__(self):
       #Init gui
       gui = Gui()
       self.window = gui.Init()
       # Events
       self.window.pattern.connect('changed', self.on_new_pattern)
       self.window.pattern.connect('activate', self.on_enter)
       self.window.matches_view.connect('row-activated', self.on_row_select)
       self.window.window.connect('delete-event', self.on_quit)
       self.window.window.connect('key-press-event', self.on_key_down)

   def main(self):
       self.playlist = commands.getoutput('/usr/bin/mpc --format "%file%" playlist').splitlines()
       self.matches = []
       self.window.pattern.emit('changed')
       gtk.main()

   def on_new_pattern(self, editable):
       self.get_matches(editable.get_text())
       self.window.matches_view.set_cursor('0')

   def on_row_select(self, treeview, path, view_column):
       iter = self.window.matches.get_iter(path)
       song_name = self.window.matches.get_value(iter, 0)
       print(song_name)
       self.play_song(song_name)

   def on_quit(self, widget, event):
       gtk.main_quit()
       return False

   def get_matches(self, pattern):
       self.window.matches.clear()
       pattern = '.*' + pattern.replace(' ', ' .*').lower()
       regexp = re.compile(pattern)
       for i in self.playlist:
           #if i.lower().find(pattern.lower()) != -1:
           if regexp.match(i.lower()):
               self.window.matches.append([i])

   def on_enter(self, entry):
       selected = self.window.matches_view.get_selection().get_selected()
       song_name = self.window.matches.get_value(selected[1], 0)
       print(song_name)
       self.play_song(song_name)
       gtk.main_quit()

   def play_song(self, name):
       commands.getoutput('mpc play "' + name + '"')
       
   def on_key_down(self, widget, event):
       if event.keyval == gtk.keysyms.Escape:
           gtk.main_quit()
           
       if event.state & gtk.gdk.CONTROL_MASK:
           if event.keyval in  (ord('n'), ord('p')):
               selected = self.window.matches_view.get_selection().get_selected()
               path = self.window.matches.get_path(selected[1])
               if event.keyval == ord('n'):
                   self.window.matches_view.set_cursor(path[0]+1)
               if event.keyval == ord('p'):
                   self.window.matches_view.set_cursor(max(0, path[0]-1))

app = Pympdfind()
app.main()

