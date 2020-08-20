from terminal import Terminal

class Video:
    def __init__(self):
        self.url = ''
        self.format = ''
        self.path = '~/Downloads'
        self.terminal = Terminal()

    def enable_formats(self):
        pass

    def download(self):
        self.terminal.download(self.url, self.format, self.path)
