shopping_list = ["milk", "pasta", "eges", "spam", "bread", "rice"]

item_to_find = "rajneesh"
found_it = None
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_it = index
#         break
if item_to_find in shopping_list:
    found_it = shopping_list.index(item_to_find)
if found_it is not None:
    print("Item to at position {}".format(found_it))
else:
    print("{} not found".format(item_to_find))