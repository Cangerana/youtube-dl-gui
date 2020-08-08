from tkinter import Event


class EventHandler():
    def __init__(self):
        self.url = ''
        self.dir_path = '~/Downloads'
        self.format = {'Video and Audio': 'bestvideo', 'Audio only': 'bestaudio'}

    def download_button_handler(self, url, format):
        self.url = url
        print(self.format[format])
        print(self.url)

    def folder_selector_handler(self, event):
        self.path = event
        print(self.path)
