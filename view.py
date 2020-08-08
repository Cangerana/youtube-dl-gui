from tkinter import *
import yt_dl_conections
from yt_dl_conections import Reader

class Window(Frame):
    def __init__(self, master=None, reader=None):
        Frame.__init__(self, master)
        self.reader = reader
        self.master = master
        self.set_geometry()
        self.set_titles('Youtube Downloader')
        # self.set_menu()
        self.set_download_button()
        self.set_url_entry()

    def set_titles(self, title):
        self.master.title(title)

    def set_geometry(self):
        self.master.geometry('640x300')

    def set_url_entry(self):
        self.url_entry = Entry(self.master, width=50, borderwidth=3)
        self.url_entry.insert(0, 'Video URL...')
        self.url_entry.pack(padx=40, ipady=5)

    def set_download_button(self):
        def click():
            reader.download_button_reader(self.url_entry.get())

        button = Button(self.master, text='Download',
                        fg='white', bg='red', command=click)
        button.place(x=525, y=250)

    def set_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit")
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)


if __name__ == '__main__':
    # App loop
    root = Tk()
    reader = Reader()
    app = Window(root, reader)
    root.mainloop()
