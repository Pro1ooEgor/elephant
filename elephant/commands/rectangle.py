from .base_classes import BaseCommand, BaseError
from .line import Line


class Rectangle(BaseCommand, BaseError):
    def create(self, x1, y1, x2, y2):
        """
        Create a new rectangle with coordinates:
        :param x1: (positive int) upper left corner
        :param y1: (positive int) upper left corner
        :param x2: (positive int) lower right corner
        :param y2: (positive int) lower right corner
        :return: list of str, that was added to the file in this step
        """
        self.check_error(self.template, x1, y1, x2, y2)

        # draw horizontal lines in our rectangle
        Line(
            file=self.file,
            template=self.template,
            character=self.character,
        ).create(x1, y1, x2, y1, is_save=False)
        Line(
            file=self.file,
            template=self.template,
            character=self.character
        ).create(x1, y2, x2, y2, is_save=False)

        # and draw vertical lines,
        # removing the corners of the intersection with the horizontal lines
        Line(
            file=self.file,
            template=self.template,
            character=self.character
        ).create(x1, y1+1, x1, y2-1, is_save=False)
        Line(
            file=self.file,
            template=self.template,
            character=self.character
        ).create(x2, y1+1, x2, y2-1, is_save=False)

        self.file.write('\n'.join(self.template) + '\n')

        return self.template
