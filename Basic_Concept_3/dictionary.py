numbers = [12, 34, 56, 78, 90]
person1 = {"Kala chan", "Chittagong", 24, "Student"}
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key: value, key: value, key: value}
person = {"name": "Ashraful", "age": 26, "city": "Dhaka", "is_student": True, "job": "Software Engineer"}
# print(person)
# print(person["job"])
# print(person.keys())
# print(person.values())

for i, num in enumerate(numbers):
    print(i, num)  # Iterating through the list with index and value

item = {"name": "Ashraful", "age": 26, "city": "Dhaka", "is_student": True}
# print(item)
item["CGPA"] = 3.57
print(item)  # Adding a new key-value pair
item["age"] = 27  # Updating an existing key-value pair
# print(item)  # Updated dictionary

# list is found from a dictionary
# print(list(item))

dic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dic)  # Creating a dictionary from a list of tuples
dic["guido"] = 5000
print(dic)  # Updated dictionary with new value for 'guido'