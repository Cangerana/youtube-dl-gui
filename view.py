from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.set_geometry()
        self.set_titles('Youtube Downloader')
        # self.set_menu()
        self.set_download_button()

    def set_titles(self, title):
        self.master.title(title)

    def set_geometry(self):
        self.master.geometry('630x320')

    def set_download_button(self):
        def click():
            click_label = Label(self.master, text='Download button was ckliked!')
            click_label.pack()
        

        button = Button(self.master, text='Download', fg='red', command=click)
        button.place(x=525, y=280)
        # button.pack()

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
    app = Window(root)
    root.mainloop()
