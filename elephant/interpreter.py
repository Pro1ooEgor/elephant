import os

from elephant.commands import BucketFill, Canvas, Line, Rectangle
from elephant.constants import (
    LINE_CHARACTER,
    LOWER_AVAILABLE_COMMANDS,
    LOWER_BUCKETFILL_COMMAND,
    LOWER_CANVAS_COMMAND,
    LOWER_LINE_COMMAND,
    LOWER_RECTANGLE_COMMAND,
    RECTANGLE_CHARACTER
)
from elephant.error import ValidationError
from elephant.utils import FindFileUtils


class Interpreter:
    def __init__(self, path_file: str, commands: list):
        self.path_file = FindFileUtils(path_file).find_path()
        self.commands = commands

    def check_errors(self):
        if not self.commands:
            raise ValidationError('Not found list of command')

        if self.commands[0].split()[0].lower() != LOWER_CANVAS_COMMAND:
            raise ValidationError('First command should create canvas')

        for command in self.commands:
            command_type = command[0].lower()
            if command_type not in LOWER_AVAILABLE_COMMANDS:
                raise ValidationError(f'Not supported command: {command_type.upper()}')

    def execute(self):
        self.check_errors()

        with open(self.path_file, 'a') as f:
            # that's used to set the state of the command execution
            template = []

            for command in self.commands:
                command = command.split()
                command_type = command[0].lower()
                command_params = [int(param) if param.isdigit() else param for param in command[1:]]

                if command_type == LOWER_CANVAS_COMMAND:
                    template = Canvas(f).create(*command_params)

                if command_type == LOWER_LINE_COMMAND:
                    character = os.environ.get(LINE_CHARACTER, 'x')
                    template = Line(
                        f,
                        template=template,
                        character=character
                    ).create(*command_params)

                if command_type == LOWER_RECTANGLE_COMMAND:
                    character = os.environ.get(RECTANGLE_CHARACTER, 'x')
                    template = Rectangle(
                        f,
                        template=template,
                        character=character
                    ).create(*command_params)

                if command_type == LOWER_BUCKETFILL_COMMAND:
                    BucketFill(
                        f,
                        template=template
                    ).create(*command_params)

        return True
