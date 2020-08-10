from tkinter import *
from tkinter import filedialog, Listbox


class Window(Frame):
    def __init__(self, master=None, handle=None):
        Frame.__init__(self, master)
        self.master = master

        self.download_path = '~/Downloads'

        self.set_geometry()
        self.set_titles()
        self.set_url_entry()
        self.set_download_button()
        self.set_folder_selector()
        self.set_format_selector()

    def set_geometry(self):
        self.master.geometry('760x200')
    
    def set_titles(self):
        self.master.title('Youtube Downloader')

    def set_url_entry(self):
        download_label = Label(self.master, text='Put the URL below')

        download_label.place(x=10 ,y=41)

        self.url_entry = Entry(self.master, width=70, borderwidth=3, highlightcolor='red')

        self.url_entry.place(x=10 ,y=61)

    def set_download_button(self):
        def donwload():
            pass

        button = Button(self.master, text='Download', fg='white', bg='red', command=donwload)

        button.place(x=645, y=150)

    def set_folder_selector(self):
        def select():
            folder_selector = filedialog.Directory(initialdir=self.download_path, title='Select a folder to download')

            folder_selector.show()

            path = folder_selector.__getattribute__('directory')
            
            if path != '':
                folder['text'] = path

        folder = Button(self.master, text=self.download_path, width=30 ,command=select)

        folder.place(x=40, y=150)

    def set_format_selector(self):
        formats = ['Video and Audio', 'Audio only']

        download_label = Label(self.master, text='Select a format')
        
        download_label.place(x=630 ,y=32)

        self.format_select = Listbox(self.master, width=14, height=2, selectbackground='red',  borderwidth=3)

        for format in formats:
            self.format_select.insert(END, format)

        self.format_select.place(x=630 ,y=52)


if __name__ == '__main__':
    root = Tk()
    app = Window(root)
    root.mainloop()
