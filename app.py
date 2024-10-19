# Task 2
# Create a file app.py and write a CLI app - a simple calculator: 
# it should be able to add and subtract two numbers.

def CLI(x: int, z: int, operation: str):
    match operation:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case _:
            return 'Unrecognised command'

