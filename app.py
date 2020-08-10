from tkinter import *

from view import Window
from yt_dl_conections import EventHandler

root = Tk()
handler = EventHandler(root)
app = Window(root, handler)
root.mainloop()
