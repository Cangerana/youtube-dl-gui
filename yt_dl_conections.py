from posix import listdir
from tkinter import Event

from os import PRIO_PGRP, fspath, system

from time import sleep

class EventHandler():
    def __init__(self, master):
        self.master = master
        self.url = ''
        self.dir_path = '~/Downloads'

    def format_selector_handler(self, url):
        """ Get the URl and return a list of possible formats"""
        if len(url) >= 11 and url[-11:].isalnum():
            system(f'youtube-dl -F {url}>>format_log') #gera um arquivo com os formatos
            all_formats = self.get_formats()
            system('rm format_log')
        else:
            return 'Url inválida'

        formats = []

        for format in all_formats:
            formats.append([format['format'], format['code'], format['extension'], format['size']])

        return formats

    def download_button_handler(self, url, format):
        self.url = url

        ls = listdir(".")

        print(f'youtube-dl -f {format} {self.url}')

        # text URL => https://www.youtube.com/watch?v=68r9ONA3pBY
        if len(format) >=2:
            system(f'youtube-dl -f {format} {self.url}')
        else:
            system(f'youtube-dl {self.url}')

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

    def get_formats(self):
        with open('format_log', 'r') as formats:
            main_format = []
            for format in formats.readlines()[3:]:
                aux_format = format.split()

                if aux_format[2] == 'audio' or aux_format[-1] == '(best)':
                    main_format.append(
                        {
                        'format': aux_format[0],
                        'extension': aux_format[1],
                        'code': aux_format[2],
                        'size': aux_format[-1] if aux_format[-1] != '(best)' else aux_format[-2]
                        }
                    )

        return main_format
