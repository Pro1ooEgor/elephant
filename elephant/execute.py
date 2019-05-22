from elephant.utils import FindFileUtils
from elephant.commands import Canvas


class CommandRunner:
    def __init__(self, path_file: str, commands: list):
        self.path_file = FindFileUtils(path_file).find_path()
        self.commands = commands

    def execute(self):
        with open(self.path_file, 'a') as f:
            print(type(f))
            Canvas(f).create()
        # for command in self.commands:
        #     print(command)
        #     command_type = command[0]
        #     if command_type.lowercase() == 'c':
        #         Canvas(
        #             x=command_type[3],
        #             y=command_type[5]
        #         )
        #     if command_type.lowercase() == 'l':
        #         some(
        #             x1=command_type[3],
        #             y1=command_type[5],
        #             x2=command_type[7],
        #             y2=command_type[9]
        #         )
        #     if command_type.lowercase() == 'r':
        #         some(
        #             x1=command_type[3],
        #             y1=command_type[5],
        #             x2=command_type[7],
        #             y2=command_type[9]
        #         )
        #     if command_type.lowercase() == 'b':
        #         some(
        #             x=command_type[3],
        #             y=command_type[5],
        #             c=command_type[7],
        #         )

