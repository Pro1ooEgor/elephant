import pytest

from elephant.utils import FindFileUtils


class TestFileUtils:
    def test_not_found_file(self):
        with pytest.raises(FileNotFoundError):
            FindFileUtils('like.file').find_path()

    def test_not_found_file_without_extension(self):
        with pytest.raises(FileNotFoundError, match='Check if the extension was transferred'):
            assert FindFileUtils('file').find_path()
