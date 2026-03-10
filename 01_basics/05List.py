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