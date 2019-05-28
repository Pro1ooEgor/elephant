from elephant.error import ValidationError
from .base_classes import BaseCommand


class Canvas(BaseCommand):
    def check_errors(self, w, h):
        if w < 0 or h < 0:
            raise ValidationError('A negative value of w or h cannot be')
        if not hasattr(self.file, 'closed'):
            raise ValidationError(f'{self.file} isn\'t file')
        if self.file.closed:
            raise ValidationError(f'File {self.file} isn\'t open')

    def create(self, w, h):
        """
        Create a new canvas of width w and height h.
        :param w: width (positive int)
        :param h: height (positive int)
        :return: list of str, that was added to the file in this step
        """
        self.check_errors(w, h)

        template = []

        template.append('-'*(w+2))
        for height in range(h):
            template.append('|' + ' '*w + '|')
        template.append('-'*(w+2))

        self.file.write('\n'.join(template) + '\n')

        return template
