


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    
    return wrapper



















def greet(name,greeting="Hello"):
    return f"{greeting}, {name}!"


greet("anas",greeting="Hi your father is here")