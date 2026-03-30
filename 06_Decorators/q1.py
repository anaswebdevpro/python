import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds called by {func.__name__}")
        return result
    
    return wrapper

@timer    
def example_fn(n):
    time.sleep(n)

    
example_fn(2)