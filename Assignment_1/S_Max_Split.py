str = input()
l_cnt = 0
r_cnt = 0
word = ""
str_list = []

for wd in str:
    if wd =="L":
        l_cnt += 1
        word += wd
    if wd == "R":
        r_cnt += 1
        word += wd
    if l_cnt == r_cnt:
        str_list.append(word)
        word = ""
        r_cnt = 0
        l_cnt = 0
print(len(str_list))
for i in str_list:
    print(i)

