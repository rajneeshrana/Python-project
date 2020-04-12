locations = {0: "You are sitting in front of computer learning python",
             1: "You are standing at the ent of a road before a small brick building",
             2: "You are top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 2, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0} }

vocabulary = { "QUIT": "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST": "E",
               "WEST": "W"}

loc = 1
while True:
    avalableExais = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + avalableExais + " ").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary[word]:
                direction = vocabulary[word]
                break
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in the direction ")