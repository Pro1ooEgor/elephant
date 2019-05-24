from elephant.utils import FindFileUtils
from elephant.commands import Canvas, Line


class CommandRunner:
    def __init__(self, path_file: str, commands: list):
        self.path_file = FindFileUtils(path_file).find_path()
        self.commands = commands

    def execute(self):
        with open(self.path_file, 'a') as f:
            # that's used for give the state to commands
            template = []

            for command in self.commands:
                command = command.split()
                command_type = command[0].lower()
                command_params = [int(param) if param.isdigit() else param for param in command[1:]]

                if command_type == 'c':
                    template = Canvas(f).create(*command_params)

                if command_type == 'l':
                    template = Line(
                        f,
                        template=template,
                        character='x'
                    ).create(*command_params)

                # if command_type.lowercase() == 'r':
                #     some(
                #         x1=command_type[3],
                #         y1=command_type[5],
                #         x2=command_type[7],
                #         y2=command_type[9]
                #     )
                # if command_type.lowercase() == 'b':
                #     some(
                #         x=command_type[3],
                #         y=command_type[5],
                #         c=command_type[7],
                #     )

