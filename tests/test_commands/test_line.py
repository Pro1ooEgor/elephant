import pytest

from elephant.commands import Line
from elephant.error import ValidationError
from tests.utils import open_file


class TestCanvas:
    def test_no_file(self):
        with pytest.raises(ValidationError, match='isn\'t file'):
            Line(
                file='like.file',
                template=['------', '|      |', '|      |', '|      |', '------'],
                character='x'
            ).create(1, 2, 3, 1)

    def test_file_closed(self):
        file = open('test_file.txt', 'a')
        file.close()
        with pytest.raises(ValidationError, match='isn\'t open'):
            Line(
                file=file,
                template=['------', '|      |', '|      |', '|      |', '------'],
                character='x'
            ).create(1, 2, 3, 1)

    @open_file('test_file.txt', 'w')
    def test_only_horizontal_line(self, tmpdir):
        with pytest.raises(ValidationError, match='Only horizontal or vertical lines are supported'):
            Line(
                file=self.file,
                template=['------', '|      |', '|      |', '|      |', '------'],
                character='x'
            ).create(1, 2, 3, 1)

    @open_file('test_file.txt', 'w')
    def test_general(self, tmpdir):
        assert Line(
                   file=self.file,
                   template=['------', '|      |', '|      |', '|      |', '------'],
                   character='x'
               ).create(1, 2, 1, 3)

    @open_file('test_file.txt', 'w')
    def test_returning_template(self, tmpdir):
        expected = ['------', '|      |', '|x     |', '|x     |', '------']
        recieved = Line(
            file=self.file,
            template=['------', '|      |', '|      |', '|      |', '------'],
            character='x'
        ).create(1, 2, 1, 3)
        assert recieved == expected

