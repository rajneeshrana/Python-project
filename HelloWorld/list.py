# ipAddress = input("Please enter your ip address")
# print(ipAddress.count("."))
# parrot_list = ["non pinin", "no more", "a stiff", "bereft a life"]
#
# parrot_list.append("a norwegian blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2,4,6,8,]
# odd = [1,3,5,7,9]
#
# numbers = even + odd
# number_in_order = sorted(numbers)
#
# print(number_in_order)
#
# if numbers == number_in_order:
#     print("the lisr are equal")
# else:
#     print("the list are not equal")
#
# if number_in_order == sorted(numbers):
#     print("the lisr are equal")
# else:
#     print("the list are not equal")

# list_1 = []
# list_2 = list()
# print("List 1: {} ".format(list_1))
# print("List 2: {}".format(list_2))
# if list_1 == list_2:
#     print("The list are equal")
#
# print(list("The list are equal"))

# even = [2,4,6,8]
# odd = [1,3,5,7,9]
#
# numbers = [even, odd]
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon",])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)