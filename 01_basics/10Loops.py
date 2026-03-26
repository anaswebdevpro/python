# here we will sess types of loops in python. and  how to use them in different ways. and best practices to use them.

# 1. for loop
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. it is used when we know the number of iterations in advance.
# syntax:
# for variable in sequence:
#     # code to be executed
# example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# 2. while loop
# while loop is used to execute a block of code as long as a specified condition is true. it is used when we don't know the number of iterations in advance.
# syntax:
# while condition:
#     # code to be executed

# example:
i = 0
while i < 5:
    print(i)
    i += 1
# 3. nested loop
# nested loop is a loop inside another loop. it is used to iterate over a sequence of
# sequences (list of lists, tuple of tuples) or other iterable objects.
# syntax:
# for variable in sequence:
#     for variable in sequence:
#         # code to be executed
# example:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)
# 4. break statement
# break statement is used to exit a loop prematurely when a certain condition is met.
# syntax:
# for variable in sequence:
#     if condition:
#         break
#     # code to be executed
# example:
for i in range(10):
    if i == 5:
        break
    print(i)
    # ------------------------------
# 5. continue statement
# continue statement is used to skip the current iteration of a loop and move to the next iteration.
# syntax:
# for variable in sequence:
#     if condition:
#         continue
#     # code to be executed
# example:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    # --------------------------------------
# 6. else statement with loops
# else statement can be used with loops to execute a block of code when the loop is finished
# syntax:
# for variable in sequence:
#     # code to be executed
# else:
#     # code to be executed when the loop is finished
# example:
for i in range(5):
    print(i)
else:
    print("Loop is finished")





