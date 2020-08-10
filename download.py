from os import system, listdir


class Video():
    """Class to find the video, download and move"""

    def __init__(self, url, format, path):
        self.url = url
        self.format = format
        self.path = path

    def download(self):
        """Download the video"""
        formats = {'Video and Audio': 'bestvideo', 'Audio only': 'bestaudio'}

        # Get all the files and folders in the diretory
        ls = listdir(".")

        if self.format == 'Audio only':
            system(f'youtube-dl -f {formats[self.format]} {self.url}')
        else:
            system(f'youtube-dl {self.url}')

        # Take a title of the video finding the new file in the diretory
        title = [file for file in listdir(".") if file not in ls].pop()

        self._move_to_dir_path(title)

    def _move_to_dir_path(self, title):
        """Take de file of download and move to select destiny file

        Args:
            title (String): Formated title
        """
        title = self._title_formater(title)
        system(f'mv {title} {self.path}/{title}')

    def _title_formater(self, title):
        """Get the original title and format it to use in terminal

        Args:
            title (String): Original title

        Returns:
            String: Formated title
        """
        title = title.replace(' ', '\ ', 20)
        title = title.replace('&', '\&', 5)
        title = title.replace("'", f"\\'", 5)
        title = title.replace('(', '\(', 5)
        title = title.replace(')', '\)', 5)
        title = title.replace('[', '\[', 5)
        title = title.replace(']', '\]', 5)

        return title
