from tkinter import Event


class EventHandler():
    def __init__(self):
        self.url = ''
        self.dir = '~/Download'

    def download_button_handler(self, event):
        self.url = event
        print(self.url)

    def folder_selector_handler(self, event):
        self.path = event
        print(self.path)