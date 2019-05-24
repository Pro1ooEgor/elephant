from .base_classes import BaseCommand, BaseError
from .line import Line


class BucketFill(BaseCommand):
    def check_error(self, x, y):
        pass

    def create(self, x, y, c: str):
        """
        Fill the entire area connected to (x,y) with "colour" c
        :param x1: (positive int)
        :param y1: (positive int)
        :param c: character that will be "color"
        :return: list of str, that was added to the file in this step
        """
        self.check_error(x, y)


        self.file.write('\n'.join(self.template) + '\n')

        return self.template
