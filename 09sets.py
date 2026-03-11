setone = {1,2,3,4,5}

settwo = {4,5,6,7,8}

#union  performs the union of two sets and returns a new set that contains all the unique elements from both sets.
print(setone.union(settwo))


#intersection  returns a new set that contains only the elements that are present in both sets.
print(setone.intersection(settwo))



#difference  returns a new set that contains only the elements that are in the first set but not in the second set.
print(setone.difference(settwo))



#symmetric_difference  returns a new set that contains only the elements that are in either set but not in both sets.
print(setone.symmetric_difference(settwo))

