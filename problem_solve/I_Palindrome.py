num = input();

def is_palindrome(s):
    return s == s[::-1]
num_str = ""
for i in num[::-1]:
   
    if len(num_str) == 0 and i == '0':
       continue
    else:       
       num_str += i
       
if is_palindrome(num):
    res = f"{num_str}\nYES"
    print(res)
    
else:
    res = f"{num_str}\nNO"
    print(res)