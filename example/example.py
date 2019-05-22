from elephant.interpretator import Interpretator
from elephant.execute import CommandRunner

print(CommandRunner('output_test.txt', Interpretator('output_test.txt').read()).execute())
