
#  *args  we can use *args to pass a variable number of arguments to a function. unlimited 
def sum(*args):   
    total = 0
    for num in args:
        total += num
    return total


result = sum(1, 2, 3, 4, 5)
print(result)