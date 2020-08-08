from tkinter import *
from tkinter import filedialog

from yt_dl_conections import EventHandler


class Window(Frame):
    def __init__(self, master=None, handle=None):
        Frame.__init__(self, master)
        self.master = master
        self.handle = handle

        self.download_path = '~/Downloads'

        self.set_geometry()
        self.set_titles('Youtube Downloader')
        self.set_url_entry()
        self.set_download_button()
        self.set_folder_selector()
        self.set_format_selector()

    def set_geometry(self):
        self.master.geometry('640x200')
    
    def set_titles(self, title):
        self.master.title(title)

    def set_url_entry(self):
        self.url_entry = Entry(self.master, width=50, borderwidth=3)
        self.url_entry.insert(0, 'Video URL...')
        self.url_entry.pack(padx=40, ipady=5)

    def set_download_button(self):
        def donwload():
            self.handle.download_button_handler(self.url_entry.get())

        button = Button(self.master, text='Download', fg='white', bg='red', command=donwload)
        button.place(x=525, y=150)

    def set_folder_selector(self):
        def select():
            folder_selector = filedialog.Directory(initialdir=self.download_path, title='Select a folder to download')
            folder_selector.show()
            path = folder_selector.__getattribute__('directory')
            
            if path != '':
                folder['text'] = path

                self.handle.folder_selector_handler(path)


        folder = Button(self.master, text=self.download_path, width=30 ,command=select)
        folder.place(x=40, y=150)

    def set_format_selector(self):
        pass


if __name__ == '__main__':
    # App loop
    root = Tk()
    handler = EventHandler()
    app = Window(root, handler)
    root.mainloop()
