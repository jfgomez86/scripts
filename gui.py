import pygtk
import gtk

class Gui:
   def Init(self):
       self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
       self.vbox = gtk.VBox()
       self.pattern = gtk.Entry()
       self.matches_scroll = gtk.ScrolledWindow()
       self.matches = gtk.ListStore(str)
       self.cell = gtk.CellRendererText()
       self.matches_column = gtk.TreeViewColumn('Matches', self.cell, text=0)
       self.matches_view = gtk.TreeView(self.matches)

       self.__set_properties()
       self.__do_layout()
       self.window.show_all()

       return self

   def __set_properties(self):
       self.window.set_title('mpdfind')
       self.window.resize(500,650)
       self.matches_scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
       self.matches_view.set_headers_visible(False)
       self.matches_view.append_column(self.matches_column)
   
   def __do_layout(self):
       self.window.add(self.vbox)
       self.vbox.pack_start(self.pattern, expand=False)
       self.vbox.pack_start(self.matches_scroll)
       self.matches_scroll.add(self.matches_view)

