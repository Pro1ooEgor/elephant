import os
from setting import RPOJECT_PATH


class Interpretator:
    def __init__(self, file_path: str):
        self.file = find_file(file_path, RPOJECT_PATH + '/')
        print(self.file)

    def read(self):
        with open('numbers.txt', 'r') as f:
            nums = f.read().splitlines()
        print(nums)

    def read_path(self, file_path):
        print(os.path.isfile(file_path))
        print(file_path)


def find_file(file_name, folder):
    # check if the path is absolute
    if os.path.isabs(file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError('Path ' + file_name + ' doesn\'t exist')
        return file_name
    # if the path relative to project directory
    if os.path.exists(os.path.join(RPOJECT_PATH, file_name)):
        return os.path.join(RPOJECT_PATH, file_name)

    # for element in os.scandir(folder):
    #     if element.is_file():
    #         if element.name == file_name:
    #             yield os.path.join(folder, element.name)
    #     else:
    #         yield from find_file(file_name, element.path)


a = find_file(os.path.join(RPOJECT_PATH, 'filex/input.txt'), RPOJECT_PATH)
print(a)
print(RPOJECT_PATH + '/' + 'files/input.txt')
print(os.path.exists(os.path.join(RPOJECT_PATH, 'files/input.txt')))

