

parrot = "Norwegian blue"
print("1. The string data type indexing")
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])

print(parrot[3])
print(parrot[6])
print(parrot[8])


print()
print("2. Negitive indexing in string")
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()

print("3. Slicing indexing string")
print(parrot)
print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:])

print()

# 4. Slicing whit Negitive number
print("4. Slicing whit Negitive number")

print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[-14:-8])

print(parrot[-11:-10])
print(parrot[-10:-9])

print()
print("5. using a step in a Slice")
print(parrot)
print(parrot[0:6:2])
print(parrot[0:6:3])
print()


number = "9,223;372:136 854:775,807"
print(number)
print(number[1::4])
seperators = number[1::4]
print(seperators)

values = "".join( char if char not in seperators else " "  for char in number).split()
print([int(val) for val in values ])