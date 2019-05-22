import os
from setting import RPOJECT_PATH


class FindFileUtils:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def find_path(self):
        # check if the path is absolute
        if os.path.isabs(self.file_path):
            if not os.path.exists(self.file_path):
                raise FileNotFoundError('Path ' + self.file_path + ' doesn\'t exist')
            return self.file_path

        # if the path relative to project directory
        if os.path.exists(os.path.join(RPOJECT_PATH, self.file_path)):
            return os.path.join(RPOJECT_PATH, self.file_path)

        def _find_by_name(file_name, folder):
            for element in os.scandir(folder):
                if element.is_file():
                    if element.name == file_name:
                        return os.path.join(folder, element.name)
                else:
                    if _find_by_name(file_name, element.path):
                        return _find_by_name(file_name, element.path)

        # try to find file in the project directory
        if _find_by_name(self.file_path, RPOJECT_PATH):
            return _find_by_name(self.file_path, RPOJECT_PATH)

        # hopelessness
        raise FileNotFoundError('File on this path ' + self.file_path + ' not found')
