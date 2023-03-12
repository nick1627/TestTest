def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x*y

def divide(x, y):
    """Division function"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x/y