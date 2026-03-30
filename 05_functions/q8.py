def print_info(**kwargs):
    """Function that accepts any keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
print_info(name="Alice", age=25, city="New York")
print_info(language="Python", level="Advanced")
