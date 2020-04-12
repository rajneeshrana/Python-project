for i in range(1, 13):
    print("No. {} squared is {} and cubes is {:4} ".format(i, i**2, i**3))
    print("*" * 80)

print()
print()

name = input("Please enter your name :")
age = int(input("How old are you, {0}? ".format(name)))

if age >= 18:
    print("you are enough to vote")
elif age == 150:
    print("sorry, yoda, you dai IN RETURN of the jedi")

else:
    print("please back in {0} years ".format(18 - age))