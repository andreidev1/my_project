def checker(check):
    def closure(x: int, y: int):
        if isinstance(x, str) or isinstance(y, str):
            raise TypeError("x and y may not be strings")
        return check(x, y)
    return closure