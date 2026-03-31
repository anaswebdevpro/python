file = open('youtube.txt', 'w')

try:
    file.write('Hello, YouTube!')
finally:
    file.close()


    
with open('youtube.txt', 'w') as file:
    file.write('Hello, YouTube!')


# -------------------------------------------------------------------

    # The enumerate() function adds a counter to an iterable and returns it in the form of an enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using the list() method.


# >>> x = ('masala','lemon','ginger')

# >>> y=enumerate(x)
# >>> y
# <enumerate object at 0x0000029D44899BC0>
# >>> list(y)
# [(0, 'masala'), (1, 'lemon'), (2, 'ginger')]
# >>> 


# opening  file in werite mode . if the file is not present it will create a new file and if the file is already present then it will overwrite the existing file.
 