Drawing tool Elepant

Program reads the input.txt, executes a set of commands from the file, step by step, and produces output.txt.


At the moment, the program support the following set of commands:

C w h   
Create Canvas: Should create a new canvas of width w and height h.  
Note: you can only draw if a canvas has been created.

L x1 y1 x2 y2  
Create Line: Should create a new line from (x1,y1) to (x2,y2). Currently only horizontal or
vertical lines are supported. Horizontal and vertical lines will be drawn using the 'x'
character.

R x1 y1 x2 y2  
Create Rectangle: Should create a new rectangle, whose upper left corner is (x1,y1) and
lower right corner is (x2,y2). Horizontal and vertical lines will be drawn using the 'x'
character.

B x y c  
Bucket Fill: Should fill the entire area connected to (x,y) with "colour" c. The behavior of this
is the same as that of the "bucket fill" tool in paint programs.

How to use  
```python
import os

from run import Elephant
from elephant.command_reader import CommandReader
from elephant.interpreter import Interpreter
```
set the characters of Line and Rectangle
```python
os.environ['RECTANGLE_CHARACTER'] = 'x'
os.environ['LINE_CHARACTER'] = 'x'
```
set the file path of input and output files
```python
input_file = 'test_input_file.txt'
output_file = 'output_test.txt'
```
read test_commands from input file
```python
commands = CommandReader(input_file).commands
```
execute test_commands
```python
Interpreter(output_file, commands).execute()
```
if you want, to write this in one string
```python
Interpreter('output_test.txt', CommandReader('test_input_file.txt').commands).execute()
```
or you can do the same just create an instance of Elephant class
and call the run method
```python
Elephant(
    input_file_path='test_input_file.txt',
    output_file_path='output_test.txt',
    line_character='x',  # optional, by default it is 'x'
    rectangle_character='x',  # optional, by default it is 'x'
).run()
```


Example  
All examples see in the dicrectory example.
