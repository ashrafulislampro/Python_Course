# List, array, collection are same terms

# index     0   1   2   3   4   5   6   7   8    9
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# index    -10 -9  -8  -7  -6  -5  -4  -3  -2   -1

# print(numbers[3], numbers[-3])

# list (start : end )   start from the start index and stop before the end index
print(numbers[2:5])  # prints elements from index 2 to 4 (
# 30, 40, 50)
print(numbers[1:7])  # prints elements from index 1 to 6 (20, 30, 40, 50, 60, 70)
print(numbers[0:10])  # prints all elements (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)


# list (start : end : step)  start from the start index and stop before the end index, incrementing by step
print(numbers[0:7:1])
print(numbers[0:7:2])  # prints every second element (10, 30, 50, 70, 90)
print(numbers[2:7:-1])  # prints elements from index 2 to 6 in reverse order (60, 50, 40, 30)
print(numbers[7:2:-1])  # prints elements from index 7 to 3 in reverse order (80, 70, 60, 50, 40)

print(numbers[4:])  # prints elements from index 4 to the end (50, 60, 70, 80, 90, 100)
print(numbers[:5])  # prints elements from the start to index 4 (10, 20, 30, 40, 50)
print(numbers[:]) # shortcut for copy a list (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(numbers[::-1]) # shortcut for reverse a list

