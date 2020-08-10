from tkinter import Event
from tkinter.constants import SEL_FIRST

from download import Video


class EventHandler():
    """Class to work with events ganerated by user"""

    def __init__(self, master):
        self.master = master

        self.url = ''
        self.output_format = ''
        self.output_path = '~/Downloads'

    def folder_select_handler(self, path):
        """Get a selected output path an analize

        Args:
            path (String): Destiny path of the download

        Returns:
            String: Processed path
        """
        if path != '' and path != ():
            self.output_path = path
        
        return self.output_path

    def download_button_event_handler(self, url=None, format=None):
        """Get the typed URL selected format when the user click in download

        Args:
            url (URL, optional): Video URL. Defaults to None.
            format (String, optional): Download format. Defaults to None.
        """
        self.output_format =  format if not None else ''
        self.url = url if not None else ''

        video = Video(self.url, self.output_format, self.output_path)
        video.download()
