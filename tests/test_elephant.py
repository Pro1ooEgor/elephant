from run import Elephant
from .constants import COMMANDS, OUTPUT


class TestInterpreter:
    def create_file(self, file_path: str, write=''):
        file = open(file_path, 'w')
        file.write(write)
        file.close()

    def retrieve_file_path(self, tmpdir, file_name='output_test.txt', write=''):
        file_path = tmpdir.join(file_name).strpath

        # Interpreter needs that the file exist
        self.create_file(file_path, write)

        return file_path

    def test_general(self, tmpdir):
        assert Elephant(
            input_file_path=self.retrieve_file_path(tmpdir, 'test_input_file.txt', write=COMMANDS),
            output_file_path=self.retrieve_file_path(tmpdir, 'output_test.txt'),
            line_character='x',
            rectangle_character='x',
        ).run()

    def test_match_template_and_file(self, tmpdir):
        input_file = self.retrieve_file_path(tmpdir, 'test_input_file.txt', write=COMMANDS)
        output_file = self.retrieve_file_path(tmpdir, 'output_test.txt')

        Elephant(
            input_file_path=input_file,
            output_file_path=output_file,
            line_character='x',
            rectangle_character='x',
        ).run()

        with open(output_file, 'r') as f:
            retrieved = f.read()

        assert retrieved == OUTPUT
