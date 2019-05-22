import _io


class Canvas:
    def __init__(self, file: _io.TextIOWrapper):
        print(type(file))
        self.file = file

    def create(self):
        self.file.write('aaa')
