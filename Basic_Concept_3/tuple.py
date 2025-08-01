def multiple():
    return 3, 4
# print(multiple())
# both values are returned as a tuple
things = "pen", "tripod", "water bottle", "charger", "phone", "web cam", "sunglass", 23, True, False, 3.23
item = ("pen", "tripod", "water bottle", "charger", "phone", "web cam", "sunglass", 23, True, False, 3.23)
# print(type(things))
# print(things[0])
# tuple is immutable, meaning it cannot be changed after creation
# print(things[1:5])
# print(things[0] = "pencil")  # This will raise an error
# print(things[-2])  # Accessing the second last item
# print(things[::])

if "phone" in things:
    print("exists")
    
mega = ([23, 2, 3], "pen", 100, [5, 7, 8])

print(mega[1])
mega[0][1] = 500  # As if tuple is immutable, but lists inside can be mutable
print(mega[0][1])  # Accessing the second item of the first list in the tuple
mega[1] = "pencil"  # This will raise an error as tuples are immutable
print(mega[1])  # This will raise an error as tuples are immutable