from posix import listdir
from tkinter import Event

from os import PRIO_PGRP, fspath, system

from time import sleep

class EventHandler():
    def __init__(self, master):
        self.master = master
        self.url = ''
        self.dir_path = '~/Downloads'
        self.format = {'Video and Audio': 'bestvideo', 'Audio only': 'bestaudio'}

    def download_button_handler(self, url, format):
        self.url = url
        ls = listdir(".")

        print(f'youtube-dl -f {self.format[format]} {self.url}')

        # text URL => https://www.youtube.com/watch?v=68r9ONA3pBY
        if format == 'Audio only':
            while (system(f'youtube-dl -f {self.format[format]} {self.url}')) != 0:
                print('loading...')
        else:
            while (system(f'youtube-dl {self.url}')) != 0:
                print('loading...')

        title = [file for file in listdir(".") if file not in ls].pop()

        self.move_to_dir_path(title)

    def folder_selector_handler(self, path):
        self.dir_path = path

    def title_formater(self, title):
        title = title.replace(' ', '\ ', 20)
        title = title.replace('&', '\&', 5)
        title = title.replace("'", f"\\'", 5)
        title = title.replace('(', '\(', 5)
        title = title.replace(')', '\)', 5)
        title = title.replace('[', '\[', 5)
        title = title.replace(']', '\]', 5)

        return title

    def move_to_dir_path(self, title):
        title = self.title_formater(title)
        print(title)
        system(f'mv {title} {self.dir_path}/{title}')
        sleep(1)
        self.quit()

    def quit(self):
        self.master.quit()
