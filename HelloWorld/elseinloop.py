numbers = [1, 45, 31, 6, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The number are unacceptable ")
        break
else:
    print("All those numbers are Fine")
