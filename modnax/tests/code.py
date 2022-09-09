
from rich.console import Console
from rich.syntax import Syntax

code = '''
""" This function says hello """
def say_hello(name):
    print(f'Hello {name}!')
# Greet me always!
for i in range(10):
    say_hello('Martin')
'''
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)

console = Console()
console.print(syntax)