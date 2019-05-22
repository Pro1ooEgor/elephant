from elephant.utils import FindFileUtils


class Interpretator:
    def __init__(self, file_path: str):
        self.file_path = FindFileUtils(file_path).find_path()
        self.open_mode = 'r'

    def read(self) -> list:
        """
        :return: list of commands reading from file
        """
        with open(self.file_path, self.open_mode) as f:
            return f.read().splitlines()
