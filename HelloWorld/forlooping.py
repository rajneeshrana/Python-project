# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)
#
# number = "9,223;372:550 897,256:346;"
# separator = " "
# for chr in number:
#     if not chr.up():
#         separator = separator + chr
# print(separator)
# print()
#
# value = "".join(chr if chr not in separator else " " for chr in number).split()
# print([int(val) for val in value])
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
         print(char, end='')