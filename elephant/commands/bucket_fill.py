import _io
import os

from elephant.error import ValidationError
from .base_classes import BaseCommand


class BucketFill(BaseCommand):
    def __init__(self, file: _io.TextIOWrapper, template: list):
        super().__init__(file, template)
        self.filling_area = {}

    def check_errors(self, x, y):
        target_coordinate = self.template[y][x]

        if not self.is_empty_area(target_coordinate):
            raise ValidationError('Not correct coordinates. '
                                  'For BucketFill need coordinates in the empty area')

    def is_empty_area(self, current_character: str):
        line_character = os.environ.get('LINE_CHARACTER', None)
        rectangle_character = os.environ.get('RECTANGLE_CHARACTER', None)

        if current_character == line_character or current_character == rectangle_character:
            return False

        return True

    def first_check_empty_area(self, x, y):
        current_state_y = []
        for index, x_character in enumerate(self.template[y][1:-1]):
            if self.is_empty_area(x_character):
                current_state_y.append(index + 1)
            elif index + 1 > x:
                break
            elif index + 1 < x:
                current_state_y.clear()
        self.filling_area[y] = current_state_y

    def check_connected_empty_area(self, last_y, current_y):
        if self.filling_area.get(last_y, False):
            state_last_y = self.filling_area[last_y].copy()
        else:
            return

        # state - is the suitable for filling area
        # and it compute on each line
        current_state_y = []
        not_in_last_state = []
        last_index_not_in_last_state = False
        for index, x_character in enumerate(self.template[current_y][1:-1]):
            if self.is_empty_area(x_character):
                if index + 1 not in state_last_y and last_index_not_in_last_state:
                    not_in_last_state.append(index + 1)
                else:
                    not_in_last_state.clear()
                current_state_y.append(index + 1)
            elif state_last_y and index + 1 <= state_last_y[0]:
                current_state_y.clear()
            elif not_in_last_state:
                current_state_y = list(set(current_state_y).difference(set(not_in_last_state)))
                not_in_last_state.clear()
            elif index + 1 not in state_last_y:
                last_index_not_in_last_state = True
            else:
                break
        if not_in_last_state:
            current_state_y = list(set(current_state_y).difference(set(not_in_last_state)))
            not_in_last_state.clear()
        if current_state_y:
            self.filling_area[current_y] = current_state_y

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

        # step 1: check the empty connected area and then
        # add it to the dictionary self.filling_area

        # check in the line that contains the coordinate passed to the command
        self.first_check_empty_area(x, y)

        # check in the lines above
        for current_y in range(len(self.template[1:y]))[::-1]:
            self.check_connected_empty_area(current_y+2, current_y+1)

        # check in the lines below
        for current_y in range(len(self.template))[y+1:-1]:
            self.check_connected_empty_area(current_y-1, current_y)

        # step 2: fill the self.template
        # according to the coordinates of the self.filing_area
        for y_index, current_y in enumerate(self.template[1:-1]):
            filling_area = self.filling_area.get(y_index+1, False)
            if filling_area:
                for x_index, current_x in enumerate(current_y):
                    if x_index in filling_area:
                        self.template[y_index+1] = ''.join((
                            self.template[y_index+1][:x_index],
                            self.character,
                            self.template[y_index+1][x_index + 1:]
                        ))

        self.file.write('\n'.join(self.template) + '\n')

        return self.template
