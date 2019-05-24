import _io


class BaseCommand:
    def __init__(self, file: _io.TextIOWrapper, template: list = None, character: str = ''):
        """
        :param file: open file
        :param template (optional): list of str, that was added to the file in the last step
        :param character (optional): a character, that is used for drawing
        """
        self.file = file
        self.template = template if template else []
        self.character = character
