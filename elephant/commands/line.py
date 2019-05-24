from elephant.error import ValidationError
from .base_command import BaseCommand


class Line(BaseCommand):
    def create(self, x1, y1, x2, y2):
        """
        Create a new line from (x1,y1) to (x2,y2)
        :param x1: width (int)
        :param y1: height (int)
        :param x2: width (int)
        :param y2: height (int)
        :return: list of str, that was added to the file in this step
        """
        if x1 != x2 and y1 != y2:
            raise ValidationError('Only horizontal or vertical lines are supported')
        if x1 == x2 and y1 == y2:
            raise ValidationError('Not correct coordinates')
        print(x1, y1, x2, y2)
        if y1 == y2:
            print(x1, x2)
            for index, x in enumerate(self.template[y1]):
                if x1 <= index <= x2:
                    # replace character with right index on character we need
                    self.template[y1] = ''.join((
                        self.template[y1][:index],
                        self.character,
                        self.template[y1][index+1:]
                    ))
        print(self.template)

        self.file.write('\n'.join(self.template) + '\n')

        return self.template

