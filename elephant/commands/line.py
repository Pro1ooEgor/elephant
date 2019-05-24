from elephant.error import ValidationError
from .base_command import BaseCommand


class Line(BaseCommand):
    def create(self, x1, y1, x2, y2):
        """
        Create a new line from (x1,y1) to (x2,y2)
        :param x1: width (positive int)
        :param y1: height (positive int)
        :param x2: width (positive int)
        :param y2: height (positive int)
        :return: list of str, that was added to the file in this step
        """
        # Error checking
        if x1 != x2 and y1 != y2:
            raise ValidationError('Only horizontal or vertical lines are supported')
        if x1 == x2 and y1 == y2:
            raise ValidationError('Not correct coordinates')
        if not self.template:
            raise ValidationError('Not found template. Give it to the class instance')
        x_len = len(self.template[0]-1)
        y_len = len(self.template-1)
        if x1 > x_len or x2 > x_len or x1 < 0 or x2 < 0 \
                or y1 > y_len or y2 > y_len or y1 < 0 or y2 < 0:
            raise ValidationError('Not correct coordinates')

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

        self.file.write('\n'.join(self.template) + '\n')

        return self.template

