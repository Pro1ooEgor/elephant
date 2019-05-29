def open_file(file_name='output_test.txt', file_mode='w'):
    """
    Open file in the pytest tmp directory

    NOTE: it needs, that tmpdir was in your method params
    e.g.
    @open_file('test_file.txt', 'w')
        def test_stuff(self, tmpdir):

    And then the open file is assigned to a class variable self.file
    Use it to work with the open file: write, read, close and other attributes and methods
    e.g.
    self.file.write('string stuff')

    Also this decorator created self.file_path variable, that contain path to file (str)
    """
    def my_decorator(func):
        def wrapped(self, tmpdir):
            self.file_path = tmpdir.join(file_name).strpath
            with open(self.file_path, file_mode) as f:
                self.file = f
                return func(self, tmpdir)
        return wrapped
    return my_decorator
