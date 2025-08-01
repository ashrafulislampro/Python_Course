# lambda

# def doubled(x):
#     return x * 2

doubled = lambda num:num* 2
squared = lambda num:num*num
result = doubled(44)
output = squared(9)

# print(result, output)
add = lambda x, y : x + y
sum = add(11, 33)
# print(sum)
numbers = [12, 56, 98, 12, 34, 56, 78, 90]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x: x * 2, numbers)
squared_nums = map(lambda x: x * x, numbers)
# print(numbers)

# print(list(doubled_nums))
# print(list(squared_nums))

actors = [
    {"name": "Sabana", "age": 65},
    {"name": "Sabnur", "age": 45},
    {"name": "Sabina", "age": 25},
    {"name": "Sabonty", "age": 38},
    {"name": "Sab", "age": 57}
]

juniors = filter(lambda actor: actor["age"]<40, actors)
fivers = filter(lambda actor: actor["age"] % 5 == 0, actors)
print(list(fivers))
print(list(juniors))
