import pytest

from elephant.commands import Rectangle
from elephant.error import ValidationError
from tests.utils import open_file


class TestCanvas:
    def test_no_file(self):
        with pytest.raises(ValidationError, match='isn\'t file'):
            Rectangle(
                file='like.file',
                template=['------', '|      |', '|      |', '|      |', '------'],
                character='x'
            ).create(1, 2, 3, 1)

    def test_file_closed(self):
        file = open('test_file.txt', 'a')
        file.close()
        with pytest.raises(ValidationError, match='isn\'t open'):
            Rectangle(
                file=file,
                template=['------', '|      |', '|      |', '|      |', '------'],
                character='x'
            ).create(1, 2, 3, 1)

    @open_file()
    def test_general(self, tmpdir):
        assert Rectangle(
            file=self.file,
            template=['------', '|      |', '|      |', '|      |', '------'],
            character='x'
        ).create(1, 2, 3, 3)

    @open_file()
    def test_returning_template(self, tmpdir):
        expected = ['------', '|xxx   |', '|x x   |', '|xxx   |', '------']
        recieved = Rectangle(
            file=self.file,
            template=['------', '|      |', '|      |', '|      |', '------'],
            character='x'
        ).create(1, 1, 3, 3)
        assert recieved == expected

