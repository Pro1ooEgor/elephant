import os

from elephant.commands import BucketFill, Canvas, Line, Rectangle
from elephant.constants import LINE_CHARACTER, RECTANGLE_CHARACTER
from elephant.error import ValidationError
from elephant.utils import FindFileUtils


class Interpreter:
    def __init__(self, path_file: str, commands: list):
        self.path_file = FindFileUtils(path_file).find_path()
        self.commands = commands

    def check_errors(self):
        if self.commands:
            if self.commands[0].split()[0].lower() != 'c':
                raise ValidationError('First command should create canvas')
        else:
            raise ValidationError('Not found list of command')

    def execute(self):
        self.check_errors()

        with open(self.path_file, 'a') as f:
            # that's used to set the state of the command execution
            template = []

            for command in self.commands:
                command = command.split()
                command_type = command[0].lower()
                command_params = [int(param) if param.isdigit() else param for param in command[1:]]

                if command_type == 'c':
                    template = Canvas(f).create(*command_params)

                if command_type == 'l':
                    character = os.environ.get(LINE_CHARACTER, 'x')
                    template = Line(
                        f,
                        template=template,
                        character=character
                    ).create(*command_params)

                if command_type == 'r':
                    character = os.environ.get(RECTANGLE_CHARACTER, 'x')
                    template = Rectangle(
                        f,
                        template=template,
                        character=character
                    ).create(*command_params)

                if command_type == 'b':
                    BucketFill(
                        f,
                        template=template
                    ).create(*command_params)

