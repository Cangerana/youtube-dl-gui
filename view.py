from tkinter import *
from tkinter import filedialog, Listbox

from yt_dl_conections import EventHandler


class Window(Frame):
    def __init__(self, master=None, handle=None):
        Frame.__init__(self, master)
        self.master = master
        self.handle = handle

        self.download_path = self.handle.dir_path

        self.set_geometry()
        self.set_titles('Youtube Downloader')
        self.set_url_entry()
        self.set_download_button()
        self.set_folder_selector()
        self.set_format_selector()

    def set_geometry(self):
        self.master.geometry('760x200')
    
    def set_titles(self, title):
        self.master.title(title)

    def set_url_entry(self):
        download_label = Label(self.master, text='Put the url below')

        download_label.place(x=10 ,y=41)

        self.url_entry = Entry(self.master, width=70, borderwidth=3, highlightcolor='red')

        self.url_entry.place(x=10 ,y=61)


    def set_download_button(self):
        def donwload():
            url = self.url_entry.get()

            format = self.format_select.get(ACTIVE)

            self.handle.download_button_handler(url, format)


        button = Button(self.master, text='Download', fg='white', bg='red', command=donwload)

        button.place(x=645, y=150)

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
        formats = ['Video and Audio', 'Audio only']

        download_label = Label(self.master, text='Selec a format')
        
        download_label.place(x=630 ,y=32)

        self.format_select = Listbox(self.master, width=14, height=2, selectbackground='red',  borderwidth=3)

        for format in formats:
            self.format_select.insert(END, format)

        self.format_select.place(x=630 ,y=52)


if __name__ == '__main__':
    root = Tk()
    handler = EventHandler()
    app = Window(root, handler)
    root.mainloop()



