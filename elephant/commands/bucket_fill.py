import _io
import os

from elephant.constants import HORIZONTAL_BORDER_CHARACTER, VERTICAL_BORDER_CHARACTER
from elephant.error import ValidationError
from .base_classes import BaseCommand


class BucketFill(BaseCommand):
    def __init__(self, file: _io.TextIOWrapper, template: list):
        super().__init__(file, template)
        self.line_character = os.environ.get('LINE_CHARACTER', None)
        self.rectangle_character = os.environ.get('RECTANGLE_CHARACTER', None)

    def check_errors(self, x, y):
        if not hasattr(self.file, 'closed'):
            raise ValidationError(f'{self.file} isn\'t file')
        if self.file.closed:
            raise ValidationError(f'File {self.file} isn\'t open')

        if not self.is_empty_character(self.template[y][x]):
            raise ValidationError(
                'Not correct coordinates. '
                'BucketFill needs the coordinates in the empty area'
            )

    def is_empty_character(self, current_character: str):
        if current_character == self.line_character \
                or current_character == self.rectangle_character \
                or current_character == HORIZONTAL_BORDER_CHARACTER \
                or current_character == VERTICAL_BORDER_CHARACTER:
            return False
        return True

    def is_connected_character(self, current_character: str):
        if current_character == self.character:
            return True
        return False

    def is_empty_area(self, x: int, y: int):
        character = self.template[y][x]
        if self.is_empty_character(character) \
                and not self.is_connected_character(character):
            return True
        return False

    def draw_on_the_template(self, x, y):
        self.template[y] = ''.join((
            self.template[y][:x],
            self.character,
            self.template[y][x + 1:]
        ))

    def check_area(self, x, y):
        # here we write the x coordinates that fall under the fill conditions
        current_x_state = []

        for index, x_character in enumerate(self.template[y][1:-1]):
            if self.is_empty_character(x_character):
                current_x_state.append(index + 1)
            elif index + 1 < x:
                current_x_state.clear()
            elif index + 1 > x:
                break

        # and then draw them on the template
        for x_index in current_x_state:
            self.draw_on_the_template(x_index, y)

        # last step is check in this (x,y) coordinate
        # one coordinate above (x, y + 1) and one below (x, y - 1)
        for x_index in current_x_state:
            if self.is_empty_area(x_index, y + 1):
                self.check_area(x_index, y + 1)
            if self.is_empty_area(x_index, y - 1):
                self.check_area(x_index, y - 1)

    def create(self, x, y, c: str):
        """
        Fill the entire area connected to (x,y) with "colour" c
        :param x: (positive int)
        :param y: (positive int)
        :param c: character that will be "color"
        :return: list of str, that was added to the file in this step
        """
        self.check_errors(x, y)
        self.character = c

        self.check_area(x, y)

        self.file.write('\n'.join(self.template) + '\n')

        return self.template
