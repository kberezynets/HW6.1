# Task 5
# Return to the main branch and create a new branch feat-div. 
# Checkout this branch and develop division support for your app. Don't forget to commit your changes.

def CLI(x: int, z: int, operation: str):
    match operation:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        case _:
            return 'Unrecognised command'
