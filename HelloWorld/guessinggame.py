import random
highest = 10
answer = random.randint(1, highest)
print(answer)

print("Please Guess number between 1 and {}:".format(highest))
guess = int(input())


if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")



# if guess < answer :
#     print("Please guess Higher ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly ")
# elif guess > answer:
#     print("Please guess lower ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")