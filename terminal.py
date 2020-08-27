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

    def get_formats(self, url):
        """ Get the URl and return a list of possible formats"""
        url = url.strip()
        if len(url) > 11:
            code = url[32:43]

        elif len(url) == 11:
            code = url

        else:
            code = 'Url Inválida!'

        print(code)

        if '!' not in code:
            system(f'youtube-dl -F {code}>>format_log') #gera um arquivo com os formatos
            all_formats = self._get_formats()
            system('rm format_log')
        else:
            return 'Url inválida'

        formats = []

        for format in all_formats:
            formats.append([format['format'], format['code'], format['extension'], format['size']])

        return formats

    def _get_formats(self):
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
        print(main_format)
        return main_format

