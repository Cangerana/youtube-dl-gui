from tkinter import Event


class Reader():
    def __init__(self):
        self.url = ''
        self.dir = '~/Download'

    def download_button_reader(self, event):
        self.url = event
        print(self.url)
