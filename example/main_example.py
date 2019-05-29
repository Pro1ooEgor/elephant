import os

from run import Elephant
from elephant.command_reader import CommandReader
from elephant.interpreter import Interpreter

# if you want to change the default 'x' character
# to "draw" Line and Rectangle, set the environment variable.
os.environ['RECTANGLE_CHARACTER'] = 'y'  # default it's 'x'
os.environ['LINE_CHARACTER'] = 'z'  # default it's 'x''

# set the file path of input and output files
input_file = 'input.txt'
output_file = 'output.txt'

# read test_commands from input file
commands = CommandReader(input_file).commands

# execute test_commands
Interpreter(output_file, commands).execute()

# if you want, to write this in one string
Interpreter('output.txt', CommandReader('input.txt').commands).execute()

# or you can do the same just create an instance of Elephant class
# and call the run method
Elephant(
    input_file_path='input.txt',
    output_file_path='output.txt',
    line_character='y',  # optional, by default it is 'x'
    rectangle_character='z',  # optional, by default it is 'x'
).run()
