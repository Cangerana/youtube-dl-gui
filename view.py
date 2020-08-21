from tkinter import *
from tkinter import filedialog, Listbox

from yt_dl_conections import EventHandler

from time import sleep

class Window(Frame):
    def __init__(self, master=None, handle=None):
        Frame.__init__(self, master)
        self.master = master

        self.handler = EventHandler(self.master)

        # Pre-sets
        self.set_geometry()
        self.set_titles()
        self.set_url_entry()
        self.set_download_button()
        self.set_folder_selector()
        self.set_format_selector()

    def set_geometry(self):
        """Set a window size"""

        self.master.geometry('760x200')
    
    def set_titles(self):
        """Set the title of the window"""        

        self.master.title('Youtube Downloader')

    def set_url_entry(self):
        """Set the area to put the url"""
        
        # Put the label above the entry box
        entry_label = Label(self.master, text='Put the URL below')
        entry_label.place(x=10 ,y=41)

        # Put the entry box in the main window
        self.url_entry = Entry(self.master, width=70, borderwidth=3, highlightcolor='red')
        self.url_entry.place(x=10 ,y=61)

    def set_download_button(self):
        """This function set the button to start the downloading, getting the
        url, format and destiny folder to download
        """

        def donwload():
            """Calling the handler"""
            url = self.url_entry.get()
            # format = self.format_select.get(ACTIVE)

            self.handler.download_button_event_handler(url=url, format=format)

        # Set button in the main window
        button = Button(self.master, text='Download', fg='white', bg='red', command=donwload)
        button.place(x=645, y=150)

    def set_folder_selector(self):
        """This function set de button to select a destiny folder
        if not select the dir='~/Downloads'
        """

        def select():
            # Open a new window to select a file
            folder_selector = filedialog.Directory(initialdir=self.handler.video.path, title='Select a folder to download')
            folder_selector.show()

            # Calling the handler
            path = folder_selector.__getattribute__('directory')
            path = self.handler.folder_select_handler(path)

            # chaging the output path to the new diretory
            folder['text'] = path

        # put the button to select a folder in the main window
        folder = Button(self.master, text=self.handler.video.path, width=30 ,command=select)
        folder.place(x=40, y=150)

    def set_format_selector(self):
        """This the button formats that call a pop-up when clicked"""

        def select():
            url = self.url_entry.get()

            formats = self.handler.format_selector_handler(url)
            if 'Url' in formats:
                self.error(formats)
            else:
                self.new_format_select(formats)

        download_label = Label(self.master, text='Select a format')

        download_label.place(x=630 ,y=32)

        self.format_select = Button(self.master, text=self.handler.video.format[1:-1] ,width=16, height=1, command=select)

        self.format_select.place(x=600 ,y=58)

    def new_format_select(self, formats):
        """Create a pop-up with the formats to user select"""

        def select():
            self.handler.video.format = format_list.get(ACTIVE)
            print(self.handler.video.format)
            new_window.destroy()
            self.set_format_selector()

        # Seting a new window
        new_window = Toplevel(self.master)
        new_window.title('Select a new format')

        format_list = Listbox(new_window, width=25, height=len(formats), selectbackground='red',  borderwidth=3)

        for format in formats:
            format_list.insert(END, format)

        format_list.grid()

        ok_button = Button(new_window, text='Select', command=select)
        ok_button.grid()

    def error(self, msg):
        def select():
            new_window.destroy()

        # Create a pop-up 
        new_window = Toplevel(self.master)

        new_window.title('Something is Wrong')
        new_window.geometry('250x75')

        error_label = Label(new_window, text=msg)
        error_label.pack(side='top')

        ok_button = Button(new_window, text='OK', command=select)
        ok_button.pack(side='bottom')
