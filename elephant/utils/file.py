import os
import sys


class FindFileUtils:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def find_path(self):
        # check if the path is absolute
        if os.path.isabs(self.file_path):
            if not os.path.exists(self.file_path):
                raise FileNotFoundError('Path ' + self.file_path + ' doesn\'t exist')
            return self.file_path

        # check the path relative to the file from which the method is called
        base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        if os.path.exists(os.path.join(base_dir, self.file_path)):
            return os.path.join(base_dir, self.file_path)

        error_message = 'File on this path "' + os.path.join(base_dir, self.file_path) + '" not found. '
        error_message += 'Check if the extension was transferred' if \
            self.file_path.find('.') == -1 else ''
        raise FileNotFoundError(error_message)
