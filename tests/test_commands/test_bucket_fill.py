import pytest

from elephant.commands import BucketFill
from elephant.error import ValidationError
from tests.utils import open_file


class TestCanvas:
    def test_no_file(self):
        with pytest.raises(ValidationError, match='isn\'t file'):
            BucketFill(
                file='like.file',
                template=['--------', '|xxx   |', '|x x   |', '|xxx   |', '--------']
            ).create(5, 1, 'o')

    def test_file_closed(self):
        file = open('test_file.txt', 'a')
        file.close()
        with pytest.raises(ValidationError, match='isn\'t open'):
            BucketFill(
                file=file,
                template=['--------', '|xxx   |', '|x x   |', '|xxx   |', '--------']
            ).create(5, 1, 'o')

    @open_file('test_file.txt', 'w')
    def test_only_horizontal_line(self, tmpdir):
        with pytest.raises(
                ValidationError,
                match='BucketFill needs the coordinates in the empty area'
        ):
            bucket_fill = BucketFill(
                file=self.file,
                template=['--------', '|xxx   |', '|x x   |', '|xxx   |', '--------']
            )

            # because the BucketFill is depends on the line and the rectangle
            # it needs to know their characters
            bucket_fill.rectangle_character = 'x'
            bucket_fill.line_character = 'x'

            bucket_fill.create(3, 1, 'o')

    @open_file('test_file.txt', 'w')
    def test_general(self, tmpdir):
        bucket_fill = BucketFill(
            file=self.file,
            template=['--------', '|xxx   |', '|x x   |', '|xxx   |', '--------']
        )
        bucket_fill.rectangle_character = 'x'
        bucket_fill.line_character = 'x'

        assert bucket_fill.create(5, 1, 'o')

    @open_file('test_file.txt', 'w')
    def test_returning_template(self, tmpdir):
        expected = ['--------', '|xxxooo|', '|x xooo|', '|xxxooo|', '--------']

        bucket_fill = BucketFill(
            file=self.file,
            template=['--------', '|xxx   |', '|x x   |', '|xxx   |', '--------']
        )
        bucket_fill.rectangle_character = 'x'
        bucket_fill.line_character = 'x'

        recieved = bucket_fill.create(5, 1, 'o')

        assert recieved == expected

