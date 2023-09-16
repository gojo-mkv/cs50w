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
for i in s:
    print(i)