user =input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {user}, you are {age} years old.")

if age < 18: 
    print("You are a minor.")
elif  age >18 and age < 30:
    print("You are an adult.")
else:
    print("You are a senior citizen.")