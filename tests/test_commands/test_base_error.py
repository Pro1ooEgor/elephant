import pytest

from elephant.commands.base_classes import BaseError
from elephant.error import ValidationError
from tests.utils import open_file


class TestBaseError:
    @open_file('test_file.txt', 'w')
    def test_not_found_template(self, tmpdir):
        with pytest.raises(ValidationError, match='Not found template'):
            BaseError().check_errors(self.file, '', 1, 1, 2, 2)

        with pytest.raises(ValidationError, match='Not found template'):
            BaseError().check_errors(self.file, [], 1, 1, 2, 2)

        with pytest.raises(ValidationError, match='Not found template'):
            BaseError().check_errors(self.file, None, 1, 1, 2, 2)

    @open_file('test_file.txt', 'w')
    def test_negative_coordinates(self, tmpdir):
        with pytest.raises(ValidationError, match='Not correct coordinates'):
            BaseError().check_errors(self.file, ['---', '| |', '---'], -1, 1, 2, 2)

        with pytest.raises(ValidationError, match='Not correct coordinates'):
            BaseError().check_errors(self.file, ['---', '| |', '---'], 1, 1, 2, -2)

    @open_file('test_file.txt', 'w')
    def test_coordinates_out_of_template(self, tmpdir):
        with pytest.raises(ValidationError, match='Not correct coordinates'):
            BaseError().check_errors(self.file, ['---', '| |', '---'], 5, 1, 2, 2)

        with pytest.raises(ValidationError, match='Not correct coordinates'):
            BaseError().check_errors(self.file, ['---', '| |', '---'], 1, 10, 12, 2)
