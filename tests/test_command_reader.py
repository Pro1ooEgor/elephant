from elephant.command_reader import CommandReader
from tests.utils import open_file


class TestCommandReader:
    def write_commands_to_file(self, file_path, commands, file_mode='w'):
        """
        :param file_path: absolute path to file
        :param commands: list of str, like ['C 20 4', 'L 1 2 6 2', 'B 10 3 o']
        where each string is one specific command
        :param file_mode: file will be open in that mode
        """
        with open(file_path, file_mode) as f:
            for command in commands:
                f.write(command + '\n')

    @open_file('input_test.txt', 'w')
    def test_returning_commands(self, tmpdir):
        commands = ['C 20 4', 'L 1 2 6 2', 'L 6 3 6 4', 'B 10 3 o', 'R 16 1 20 3', 'B 10 3 o']

        for command in commands:
            self.file.write(command + '\n')

        # to save the commands in the file that are read further
        # need to close the file
        self.file.close()

        recieved_commands = CommandReader(
            file_path=self.file_path
        ).commands

        assert commands == recieved_commands

