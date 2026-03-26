l1=[1,2,3,4,5,6]
l2=l1
print(l1)
print(l2)


l1[0]=100
print(l1)
print(l2)


print("to avoid this we can use copy method")

r1=[1,2,3,4,5,6]
r2 =r1[:]
print(r1)
print(r2)

r1[0]=100
print(r1)
print(r2)



# comprehesive way to generate a list
# syntax:
# [expression for item in iterable if condition]

# example:
squares = [x**2 for x in range(10)]
print(squares)


# here is the table of  list methods:  first column is the method name, second column is the description of the method, third column is the example of the method.


# ===== LIST METHODS WITH USE CASES AND BEST PRACTICES =====

print("| Method    | Description                                | Example                              |")
print("|-----------|--------------------------------------------|------------------------------------|")
print("| append()  | Adds an element to the end of the list     | list.append('item')                |")
print("| insert()  | Adds an element at a specific position     | list.insert(0, 'item')             |")
print("| remove()  | Removes first occurrence of an element     | list.remove('item')                |")
print("| pop()     | Removes and returns the last element       | item = list.pop()                  |")
print("| clear()   | Removes all elements from the list         | list.clear()                       |")
print("| index()   | Returns the index of first occurrence      | pos = list.index('item')           |")
print("| count()   | Returns number of occurrences              | count = list.count('item')         |")
print("| sort()    | Sorts elements in ascending order          | list.sort()                        |")
print("| reverse() | Reverses the order of elements             | list.reverse()                     |")

# Example usage:
shopping_cart = ['apple', 'banana']
shopping_cart.append('orange')
print("\nappend example:", shopping_cart)

tasks = ['task2', 'task3']
tasks.insert(0, 'task1')
print("insert example:", tasks)

shopping_cart.remove('banana')
print("remove example:", shopping_cart)

last_task = tasks.pop()
print("pop example:", last_task)

scores = [45, 23, 67, 12, 89]
scores.sort()
print("sort example:", scores)
