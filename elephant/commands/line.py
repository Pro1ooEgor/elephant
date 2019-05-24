from elephant.error import ValidationError
from .base_classes import BaseCommand, BaseError


class Line(BaseCommand, BaseError):
    def check_error(self, x1, y1, x2, y2):
        super().check_error(self.template, x1, y1, x2, y2)

        # currently
        if x1 != x2 and y1 != y2:
            raise ValidationError('Only horizontal or vertical lines are supported')

    def create(self, x1, y1, x2, y2, is_save=True):
        """
        Create a new line from (x1,y1) to (x2,y2)
        :param x1: (positive int)
        :param y1: (positive int)
        :param x2: (positive int)
        :param y2: (positive int)
        :param is_save: (optional) is_save=False is ability to add a line
        to the template without saving to the file
        :return: list of str, that was added to the file in this step
        """
        self.check_error(x1, y1, x2, y2)

        if y1 == y2:
            for index, x in enumerate(self.template[y1]):
                if x1 <= index <= x2:
                    self.template[y1] = ''.join((
                        self.template[y1][:index],
                        self.character,
                        self.template[y1][index+1:]
                    ))

        if x1 == x2:
            for index, y in enumerate(self.template):
                if y1 <= index <= y2:
                    self.template[index] = ''.join((
                        self.template[index][:x1],
                        self.character,
                        self.template[index][x1+1:]
                    ))
        if is_save:
            self.file.write('\n'.join(self.template) + '\n')

        return self.template

