from function import double_it as dt
from kargs_multiple import full_name as fn
from default_args import *

add = sum(300, 400)
print("Sum of 300 and 400 is: ", add)
name = fn("John", "Doe")
print("Full name : ", name)  # This will print "John Doe"
result = dt(100)
print(result)