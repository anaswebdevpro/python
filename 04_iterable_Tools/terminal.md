# Basic way to read file

# >>> x =open('file.py')

# >>> x.readline()         'import time \n'
# >>> x.readline()          'print("chai is here")\n'
# >>> x.readline()          'username ="anas"\n'
# >>> x.readline()          'print(username)'
# >>> x.readline()           ''        due to end of file it handle it by empty string  StopIteration()

<!-- to clear terminal in python we use  -->
behind the scene it works as like this 
we use .nextline() to avoid the stop iteration error. 
.nextline() handle the stopiteration error by returning empy stirng 

PS E:\python\04_iterable_Tools> python3

>>> x= open('file.py')
>>> x.__next__()           'import time \n'
>>> x.__next__()           'print("chai is here")\n'
>>> x.__next__()           'username ="anas"\n'
>>> x.__next__()           'print(username)'
>>> x.__next__()            Traceback (most recent call last):
                            File "<stdin>", line 1, in <module>
                            x.__next__()
                            StopIteration


<!-- using for loop  -->
    >>> for line in open('file.py'):
...     print(line)
... 
import time 

print("chai is here")

username ="anas"

print(username)

