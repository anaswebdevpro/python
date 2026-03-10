# Data types / object types

-Number: int, float, complex :1234,3.234, 2+3j 0b11, Decimal(),Fraction()

example :
a= 20
print(a)

b= 3.14
print(b)
c= 2+3j
print(c)

# Boolean: bool

example :
is_valid = True
print(is_valid)
is_empty = False
print(is_empty)

# String: str

example :
name = "Alice"
print(name)
greeting = 'Hello, World!'
print(greeting)

# List: list

example :
fruits = ["apple", "banana", "cherry"]
print(fruits)

we can store different data types in a list even list inside list
example :
my_list = [1, "hello", 3.14, [1, 2, 3]]
print(my_list)
output : [1, 'hello', 3.14, [1, 2, 3]]

# Tuple: tuple

Touple is similar to list but it is immutable (cannot be changed after creation)
IT is used to store multiple items in a single variable and it is ordered and unchangeable
example :
point = (2, 3)
print(point)

# Dictionary: dict

Dictionary is a collection of key-value pairs and it is unordered, changeable and indexed

 we can store different data types in a dictionary and it is used to store data values like a map, which unlike other data types that hold only a single value as an element, dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

example :
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)

# Set: set

Set is a collection which is unordered, unchangeable\*, and unindexed. No duplicate

it will ignoure is you try to add duplicate value in set it will ignore the duplicate value and it will not give any error

example :
my_set = {1, 2, 3, 4, 5}
print(my_set)

# None: NoneType

 None is a special constant in Python that represents the absence of a value or a null value

example :
my_var = None
print(my_var)
