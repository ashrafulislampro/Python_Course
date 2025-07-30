num1, num2 = map(int, input().split())

def is_lucky_number(n):
    while n != 0:
        tmp = n % 10
        if tmp != 4 and tmp != 7:
            return False
        n //= 10
    return True

found = False
for i in range(num1, num2 + 1):
    if is_lucky_number(i):
        print(i, end=' ')
        found = True

if not found:
    print(-1)
