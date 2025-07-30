numbers = [35, 21, 25, 40, 45, 50, 65, 96,55]
odds = []

for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
# print(odds)

odd_nums = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
# print(odd_nums)

players = ["Tamim", "Mushfiq", "Riyad"]
ages = [30, 28, 32]

age_cmb = []

for pl in players:
    for age in ages:
        # print(pl, age)
        age_cmb.append([pl, age])
        
        
print(age_cmb)

age_cmb2 = [[player, age] for player in players for age in ages]
print(age_cmb2)

