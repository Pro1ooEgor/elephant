import os

from elephant.command_reader import CommandReader
from elephant.constants import LINE_CHARACTER, RECTANGLE_CHARACTER
from elephant.interpreter import Interpreter
from elephant.utils import FindFileUtils


class Elephant:
    def __init__(
            self,
            input_file_path: str,
            output_file_path: str,
            line_character: str = 'x',
            rectangle_character: str = 'x'
    ):
        self.input_file_path = FindFileUtils(input_file_path).find_path()
        self.output_file_path = FindFileUtils(output_file_path).find_path()
        # characters, that the tool "draws"
        self.line_character = line_character
        self.rectangle_character = rectangle_character

    def run(self):
        # set the characters of Line and Rectangle
        os.environ[LINE_CHARACTER] = self.rectangle_character
        os.environ[RECTANGLE_CHARACTER] = self.line_character

        # read test_commands from input file
        self.commands = CommandReader(self.input_file_path).commands

        # execute test_commands
        Interpreter(self.output_file_path, self.commands).execute()

        return True
