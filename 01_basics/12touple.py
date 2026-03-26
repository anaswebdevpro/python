# TUPLES - Immutable sequences in Python

# 1. CREATING TUPLES
print("=== CREATING TUPLES ===")
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1, "mixed", 3.14)
t4 = tuple([1, 2, 3])  # Convert list to tuple
t5 = (42,)  # Single element tuple (comma required)
t6 = ()  # Empty tuple

print(f"t1: {t1}")
print(f"t5: {t5}\n")

# 2. TUPLE METHODS
print("=== TUPLE METHODS ===")

# count() - Returns number of occurrences
t = (1, 2, 2, 3, 2, 4)
print(f"count(2): {t.count(2)}")  # Output: 3

# index() - Returns index of first occurrence
print(f"index(3): {t.index(3)}")  # Output: 3

# 3. ACCESSING ELEMENTS
print("\n=== ACCESSING ELEMENTS ===")
fruits = ("apple", "banana", "cherry")
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}\n")

# 4. UNPACKING
print("=== UNPACKING ===")
a, b, c = ("x", "y", "z")
print(f"a={a}, b={b}, c={c}\n")

# 5. IMMUTABILITY (Key Benefit)
print("=== IMMUTABILITY ===")
t = (1, 2, 3)
print(f"Original: {t}")
# t[0] = 99  # This would cause: TypeError: 'tuple' object does not support item assignment
print("Tuples CANNOT be modified!\n")

# 6. USE CASES
print("=== PRACTICAL USE CASES ===")

# Dictionary keys (tuples work, lists don't)
coords = {(0, 0): "origin", (1, 2): "point A"}
print(f"Dict with tuple keys: {coords}")

# Function returns multiple values
def get_user():
    return ("John", 25, "john@email.com")

name, age, email = get_user()
print(f"User: {name}, {age}, {email}")

# Protecting data from accidental modification
config = ("localhost", 8080, "production")
print(f"Config (safe): {config}")