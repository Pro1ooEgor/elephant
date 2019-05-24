from elephant.interpretator import Interpretator
from elephant.execute import CommandRunner

print(CommandRunner('output_test.txt', Interpretator('input.txt').read()).execute())
