import pytest

from elephant.commands import Canvas
from elephant.error import ValidationError
from tests.utils import open_file


class TestCanvas:
    def test_no_file(self):
        with pytest.raises(ValidationError, match='isn\'t file'):
            Canvas('like file').create(1, 2)

    def test_file_closed(self, tmpdir):
        file = open(tmpdir.join('test_file.txt').strpath, 'w')
        file.close()
        with pytest.raises(ValidationError, match='isn\'t open'):
            Canvas(file).create(1, 2)

    def test_negative_value(self):
        with pytest.raises(ValidationError, match='A negative value of w or h cannot be'):
            Canvas('like file').create(-2, -3)

        with pytest.raises(ValidationError, match='A negative value of w or h cannot be'):
            Canvas('like file').create(-2, 1)

        with pytest.raises(ValidationError, match='A negative value of w or h cannot be'):
            Canvas('like file').create(1, -2)

    @open_file('test_file.txt', 'w')
    def test_general(self, tmpdir):
        assert Canvas(self.file).create(1, 2)

    @open_file('test_file.txt', 'w')
    def test_returning_template(self, tmpdir):
        expected = ['---', '| |', '---']
        assert Canvas(self.file).create(1, 1) == expected

