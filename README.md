
# Drawing tool Elephant

Program reads the input.txt, executes a set of commands from the file, step by step, and produces output.txt.  

 - [Commands](#commands)
 - [How to use](#how-to-use)
     - [Main class](#main-class)
     - [More detail](#more-detail)
     - [Detail short way](#detail-short-way)
 - [Examples](#examples)
 
## Commands
At the moment, the program support the following set of commands:  
  
C w h     
Create Canvas: Create a new canvas of width w and height h.    
Note: you can only draw if a canvas has been created.  
  
L x1 y1 x2 y2    
Create Line: Create a new line from (x1,y1) to (x2,y2). Currently only horizontal or  
vertical lines are supported. Horizontal and vertical lines will be drawn using the 'x'  
character.  
  
R x1 y1 x2 y2    
Create Rectangle: Create a new rectangle, whose upper left corner is (x1,y1) and  
lower right corner is (x2,y2). Horizontal and vertical lines will be drawn using the 'x'  
character.  
  
B x y c    
Bucket Fill: Fill the entire area connected to (x,y) with "colour" c. The behavior of this  
is the same as that of the "bucket fill" tool in paint programs.  
  
## How to use    
### Main class
Create an instance of Elephant class and call the run method.  
```python  
from run import Elephant 

Elephant(  
  input_file_path='test_input_file.txt',  
  output_file_path='output_test.txt',  
  line_character='y',  # optional, by default it is 'x'  
  rectangle_character='z',  # optional, by default it is 'x'  
).run()  
```  
### More detail
Another longer way to do same.

If you want to change the default 'x' character to "draw" Line and Rectangle, set the environment variable.
```python  
import os 

os.environ['RECTANGLE_CHARACTER'] = 'y'  # default it's 'x'
os.environ['LINE_CHARACTER'] = 'z'  # default it's 'x'
```  
And then set the file path of input and output files.  
```python  
input_file = 'input.txt'  
output_file = 'output.txt'  
```  
Read commands from input file.  
```python  
from elephant.command_reader import CommandReader 

commands = CommandReader(input_file).commands  
```  
Execute commands  
```python  
from elephant.interpreter import Interpreter  

Interpreter(output_file, commands).execute()  
```  
### Detail short way
If you want, to write the way above in one string.  
```python  
from elephant.command_reader import CommandReader  
from elephant.interpreter import Interpreter

Interpreter('output.txt', CommandReader('test.txt').commands).execute()  
```

## Examples    
All examples see in the directory example.
