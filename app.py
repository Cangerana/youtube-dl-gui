from tkinter import Tk

from view import Window

class App():
    """Main class of the program"""

    def __init__(self):
        self.master = Tk()
        self.window = Window(self.master)
        self.run()

    def run(self):
        """This function start the program"""
        self.master.mainloop()


if __name__ == '__main__':
    main = App()