from os import system, listdir


class Terminal():
    """Class to find the video, download and move"""

    def _move_to_dir_path(self, title, path):
        """Take de file of download and move to select destiny file

        Args:
            title: str
        """
        def title_formater(title):
            """Get the original title and format it to use in terminal"""
            title = title.replace(' ', '\ ', 20)
            title = title.replace('&', '\&', 5)
            title = title.replace("'", f"\\'", 5)
            title = title.replace('(', '\(', 5)
            title = title.replace(')', '\)', 5)
            title = title.replace('[', '\[', 5)
            title = title.replace(']', '\]', 5)

            return title

        title = title_formater(title)
        system(f'mv {title} {path}/{title}')

    def download(self, url, format, path):
        """Download the video"""
        formats = {'Video and Audio': 'bestvideo', 'Audio only': 'bestaudio'}

        # Get all the files and folders in the diretory
        ls = listdir(".")

        if format == 'Audio only':
            system(f'youtube-dl -f {formats[format]} {url}')
        else:
            system(f'youtube-dl {url}')

        # Take a title of the video finding the new file in the diretory
        title = [file for file in listdir(".") if file not in ls].pop()

        self._move_to_dir_path(title, path)
