import os

from run import Elephant
from elephant.command_reader import CommandReader
from elephant.interpreter import Interpreter

# set the characters of Line and Rectangle
os.environ['RECTANGLE_CHARACTER'] = 'x'
os.environ['LINE_CHARACTER'] = 'x'

# set the file path of input and output files
input_file = 'test_input_file.txt'
output_file = 'output_test.txt'

# read commands from input file
commands = CommandReader(input_file).commands

# execute commands
Interpreter(output_file, commands).execute()

# if you want, to write this in one string
Interpreter('output_test.txt', CommandReader('test_input_file.txt').commands).execute()

# or you can do the same just create an instance of Elephant class
# and call the run method
Elephant(
    input_file_path='test_input_file.txt',
    output_file_path='output_test.txt',
    line_character='x',  # optional, by default it is 'x'
    rectangle_character='x',  # optional, by default it is 'x'
).run()
