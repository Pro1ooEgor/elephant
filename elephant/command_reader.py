from elephant.utils import FindFileUtils


class CommandReader:
    def __init__(self, file_path: str, open_mode='r'):
        self.file_path = FindFileUtils(file_path).find_path()
        self.open_mode = open_mode

    @property
    def commands(self) -> list:
        """
        :return: list of test_commands read from file
        """
        with open(self.file_path, self.open_mode) as f:
            return f.read().splitlines()
