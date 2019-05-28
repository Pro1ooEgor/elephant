import pytest

from elephant.commands import Canvas
from elephant.error import ValidationError


class TestFileUtils:
    def test_negative_value(self):
        with pytest.raises(ValidationError, match='A negative value of w or h cannot be'):
            Canvas('like file').create(-2, -3)

        with pytest.raises(ValidationError, match='A negative value of w or h cannot be'):
            Canvas('like file').create(-2, 1)

        with pytest.raises(ValidationError, match='A negative value of w or h cannot be'):
            Canvas('like file').create(1, -2)

    def test_no_file(self):
        with pytest.raises(ValidationError, match='isn\'t file'):
            Canvas('like file').create(1, 2)

    def test_file_closed(self):
        file = open('test_file.txt', 'a')
        file.close()
        with pytest.raises(ValidationError, match='isn\'t open'):
            Canvas(file).create(1, 2)

    def test_general(self):
        import os
        with open('test_file.txt', 'a') as f:
            assert Canvas(f).create(1, 2)

