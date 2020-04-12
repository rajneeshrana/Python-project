fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

# ordred_key = list(fruit.keys())
# ordred_key.sort()
# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])
# for i in sorted(fruit.keys()):
for i in fruit:
    print(i + " - " + fruit[i])
    print("-" * 50)