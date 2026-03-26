
# ============================================================
# DICTIONARY METHODS QUICK TABLE (commented reference)
# ============================================================
# | Method                  | Best-Practice Use Case                              | Example |
# |-------------------------|-----------------------------------------------------|---------|
# | get(key, default)       | Safe read without KeyError                          | price = data.get("price", 0) |
# | setdefault(key, value)  | Create key only if missing                          | visits.setdefault("user1", 0) |
# | keys()                  | Iterate only keys                                   | for k in data.keys(): ... |
# | values()                | Iterate only values                                 | for v in data.values(): ... |
# | items()                 | Iterate key + value together                        | for k, v in data.items(): ... |
# | update(other_dict)      | Merge/overwrite from another dict                   | user.update({"age": 25}) |
# | pop(key, default)       | Remove key and get value safely                     | qty = cart.pop("apple", 0) |
# | popitem()               | Remove last inserted pair (LIFO)                    | last = data.popitem() |
# | copy()                  | Shallow copy before changing data                   | backup = data.copy() |
# | clear()                 | Empty dictionary while keeping same variable        | data.clear() |
# | fromkeys(keys, value)   | Build dict with same initial value                  | flags = dict.fromkeys(["a","b"], False) |
#
# BEST PRACTICES:
# 1) Prefer .get() for optional keys to avoid KeyError.
#    score = student.get("score", 0)
#
# 2) Use .items() when you need both key and value (cleaner and faster).
#    for car, count in garage.items():
#        print(car, count)
#
# 3) Keep key types consistent in one dictionary (all strings, all ints, etc.).
#    Good: {"name": "Ali", "city": "Lahore"}
#    Avoid: {"name": "Ali", 1: "Lahore"}
#
# 4) Use descriptive keys for readability.
#    profile = {"first_name": "Sara", "is_active": True}
#
# 5) Use nested dictionaries for structured data.
#    employee = {"id": 1, "contact": {"email": "a@b.com", "phone": "123"}}
#
# # dictionaries: unordered collections of data in key-value pairs, similar to objects in JavaScript
# # syntax : dict_name = {key1:value1,key2:value2,.....}
# # example:
# person = {"name": "John", "age": 30, "city": "New York"}
# print(person)

# # accessing values in a dictionary
# print(person["name"])
# print(person.get("age"))
# # adding new key value pair to a dictionary
# person["country"] = "USA"
# print(person)
# # updating value of a key in a dictionary
# person["age"] = 31
# print(person)
# # removing key value pair from a dictionary
# del person["city"]
# print(person)
# # looping through a dictionary
# for key in person:
#     print(key, person[key])
# for key, value in person.items():
#     print(key, value)


garage ={ "Mercedes": 2, "BMW": 3, "Audi": 1 , "Toyota": 4, "Honda": 5, "Bike":"kawasaki", "Scooter":"vespa",  "Electric Car":"Tesla Model S", "Hybrid Car":"Toyota Prius", "Diesel Car":"Volkswagen Passat TDI"}


#  for loop acess key and values in a dictionary

for key in garage:
    print(key, garage[key], end=" \n ")

#  for loop with items() method to access key and values in a dictionary
for key, value in garage.items():
    print(key, value, end=" \n ")


    # question: how to check if a key is in a dictionary?
if "Mercedes" in garage:
    print("Mercedes is in the garage")
print(len(garage))