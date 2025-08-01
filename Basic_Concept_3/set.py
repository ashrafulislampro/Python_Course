basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)  # Duplicates are removed, only unique items remain

res = "grape" in basket
# res = "orange" in basket
# print(res)  # Check if 'orange' is in the set   

a = set('abracadabra')
b = set('alacazam')
# print(a)  # Unique characters from 'abracadabra'
# print(b)
print(a - b)  # Characters in 'a' but not in 'b'
print(a | b)  # Characters in either 'a' or 'b'
print(a & b)  # Characters in both 'a' and 'b'
print(a ^ b)  # Characters in either 'a' or 'b' but not both