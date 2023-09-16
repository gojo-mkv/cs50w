name = input("Name: ")
print(f"Hello, {name}!")

# Tuple: a pair of immutable values
coordinate = (10.0, 20.0)

#List
names = ["Harry", "Ron"]
names.append("Hermione")
names.sort()
print(names)

# Set
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)
s.remove(3)
print(s)
print(f"The set has {len(s)} elements")

# For loop
for element in s:
    print(element)

# Dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])
houses["Hermione"] = "Gryffindor"

# Functions
def square(x):
    return x * x
for i in range(10):
    print(f"The square of {i} is {square(i)}")

# To import from another file, use
    # from filename import function_name
# Or
    # import filename
    # filename.function_name()

# Exceptions
x = int(input("x:"))
y = int(input("y:"))

try:
    result = x / y
    print(result)
except ZeroDivisionError:   # Or ValueErro
    print("Cannot divide by 0")