# name = "abcdefghijklmnopqrstuvwxyz"
#
# print(name)
# print(name[16:13:-1])
# print(name[4::-1])
# print(name[:-9:-1])
#
# print(name[-4:])
# print(name[-1:])
# print(name[:1])
# print(name[0])
#
#
# meal1 = "spam" + "eggs" + "beans"
# meal2 = "spam\neggs\nbeans"
# meal3 = "spam, eggs, beans"
# meal4 = """spam
# eggs
# beans"""
# print(meal1)
# print(meal2)
# print(meal3)
# print(meal4)
#
# print(45-15 / 3)
# print(30 / 3)


# guess game start
# import random
# highest = 10
# answer = random.randint(1, highest)
# print(answer)  #TODO: Remove after testing
# guess = 0 # initialise  to any number   that does't equal the answer
# print("Please Guess number between 1 and {}:".format(highest))
#
# while guess != answer:
#     guess = int(input())
#
#     if guess == answer:
#         print("Well done, you guessed it")
#         break
#
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         else:  # guess must be greater than answer
#             print("Please guess lower")
#         # guess = int(input())
#         # if guess == answer:
#         #     print("Well done, you guessed it")
#         # else:
        #     print("Sorry, you have not guessed correctly")

# guess game end


number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer += number

print(answer)