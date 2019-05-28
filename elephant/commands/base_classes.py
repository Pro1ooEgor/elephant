import _io

from elephant.error import ValidationError


class BaseCommand:
    def __init__(self, file: _io.TextIOWrapper, template: list = None, character: str = ' '):
        """
        :param file: open file
        :param template: (optional) list of str, that was added to the file in the last step
        :param character: (optional) a character, that is used for drawing
        """
        self.file = file
        self.template = template if template else []
        self.character = character


class BaseError:
    @staticmethod
    def check_errors(template, x1, y1, x2, y2):
        if not template:
            raise ValidationError('Not found template. Give it to the class instance')

        x_len = len(template[0]) - 1
        y_len = len(template) - 1
        if x1 > x_len or x2 > x_len or x1 < 0 or x2 < 0 \
                or y1 > y_len or y2 > y_len or y1 < 0 or y2 < 0:
            raise ValidationError('Not correct coordinates')
