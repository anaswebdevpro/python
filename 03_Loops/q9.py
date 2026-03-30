items = ['apple', 'banana', 'cherry', 'date', 'elderberry','apple', 'banana']


# for item in items:
#     if items.count(item) > 1:
#         print(item)
#         break

unique_items = set()

for item  in items:
    if item in unique_items:
        print(" Duplicate item found:", item)
        break
    unique_items.add(item)
    # print(unique_items)