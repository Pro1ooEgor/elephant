import pytest

from elephant.interpreter import Interpreter
from elephant.error import ValidationError
from .constants import OUTPUT


class TestInterpreter:
    def create_file(self, file_path: str):
        open(file_path, 'w').close()

    def retrieve_file_path(self, tmpdir, file_name='output_test.txt'):
        file_path = tmpdir.join(file_name).strpath

        # Interpreter needs that the file exist
        self.create_file(file_path)

        return file_path

    def test_no_commands(self, tmpdir):
        commands = []

        with pytest.raises(ValidationError, match='Not found list of command'):
            Interpreter(
                path_file=self.retrieve_file_path(tmpdir),
                commands=commands
            ).execute()

    def test_not_supported_commands(self, tmpdir):
        commands = ['C 20 4', 'O 1 2 3']
        with pytest.raises(ValidationError, match='Not supported command'):
            Interpreter(
                path_file=self.retrieve_file_path(tmpdir),
                commands=commands
            ).execute()

        commands = ['C 20 4', 'Q', 'L 1 2 6 2']
        with pytest.raises(ValidationError, match='Not supported command'):
            Interpreter(
                path_file=self.retrieve_file_path(tmpdir),
                commands=commands
            ).execute()

        commands = ['C 20 4', '1 2', 'L 1 2 6 2']
        with pytest.raises(ValidationError, match='Not supported command'):
            Interpreter(
                path_file=self.retrieve_file_path(tmpdir),
                commands=commands
            ).execute()

    def test_first_command(self, tmpdir):
        commands = ['L 1 2 6 2', 'B 10 3 o', 'R 16 1 20 3', 'B 10 3 o']

        with pytest.raises(ValidationError, match='First command should create canvas'):
            Interpreter(
                path_file=self.retrieve_file_path(tmpdir),
                commands=commands
            ).execute()

    def test_general(self, tmpdir):
        commands = ['C 20 4', 'L 1 2 6 2', 'B 10 3 o', 'R 16 1 20 3', 'B 10 3 o']

        assert Interpreter(
                path_file=self.retrieve_file_path(tmpdir),
                commands=commands
            ).execute()

    def test_match_template_and_file(self, tmpdir):
        commands = ['C 20 4', 'L 1 2 6 2', 'L 6 3 6 4', 'R 16 1 20 3', 'B 10 3 o']
        file_path = self.retrieve_file_path(tmpdir)

        Interpreter(
            path_file=file_path,
            commands=commands
        ).execute()

        with open(file_path, 'r') as f:
            retrieved = f.read()

        assert retrieved == OUTPUT

