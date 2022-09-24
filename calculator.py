from decorators.checker import checker

@checker
def suma(x: int, y: int) -> int:
    return x + y

@checker
def substract(x: int, y: int) -> int:
    return x - y

@checker
def divide(x: int, y: int) -> int:
    return x // y

@checker
def multiply(x: int, y: int) -> int:
    return x * y


