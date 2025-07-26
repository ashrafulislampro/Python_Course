#  Onek gula parameter pass without key. just value pass

def name2(first, *args):
    print(args)
    return first;

name1 = name2("John", "Doe", "Smith", "Brown")
print(name1)  # This will print "John"

def full_name(first, last):
    return f"{first} {last}"

# name0 = full_name("John", "Doe",)
# name = full_name(last="Doe", first="John")
# print(name)  # This will print "John Doe"

# Onek gula parameter key akare dichh **kargs
def famous_name(first, last, **addition):
    full = f"{first} {last}"
    # print(addition)
    for key, value in addition.items():
        print(key, value)
    return full
    
names = famous_name(first="Tahery", last= "Ali", title="Hujor",title2="matabor", title3="funny_man", addition="pagla")
# print(names)  # This will print "Tahery Ali"

# multiple value return from a function
def a_lot(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div
everything = a_lot(10, 3)
print(everything)