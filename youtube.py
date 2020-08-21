from terminal import Terminal

class Video:
    def __init__(self):
        self.url = ''
        self.format = ' video and audio '
        self.path = '~/Downloads'
        self.terminal = Terminal()

    def enable_formats(self):
        return self.terminal.get_formats(self.url)

    def download(self):
        self.terminal.download(self.url, self.format, self.path)

    def url_validate(self):
        pass