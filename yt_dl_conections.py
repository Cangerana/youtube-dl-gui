from tkinter import Event
from tkinter.constants import SEL_FIRST

from youtube import Video


class EventHandler():
    """Class to work with events ganerated by user"""

    def __init__(self, master):
        self.master = master
        self.video = Video()

    def folder_select_handler(self, path):
        """Valid the selected destiny path
        Args:
            path: str

        Returns:
            path: str
        """
        if path != '' and path != ():
            self.video.path = path
        
        return self.video.path

    def download_button_event_handler(self, url=None, format=None):
        """Get the typed URL selected format when the user click in download

        Args:
            url: str
            format: str (optional)
        """
        format =  format if not None else ''
        url = url if not None else ''

        self.video.url = url
        self.output_format = format

        self.video.download()
