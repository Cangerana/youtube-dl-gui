from tkinter import Event
from tkinter.constants import SEL_FIRST


class EventHandler():
    """Class to work with events ganerated by user"""

    def __init__(self, master):
        self.master = master

        self.url = ''
        self.output_format = ''
        self.output_path = '~/Downloads'

    def folder_select_handler(self, path):
        if path != '':
            self.output_path = path
        
        return self.output_path

    def download_button_event_handler(self, url=None, format=None):
        print('clicked!')
        print(self.output_path)
