num = int(input())
arr = list(map(int, input().split()))

def min_operation(n):
    cnt = 0
    while n > 0:
        n /= 2
        if n % 2 == 0:
            cnt +=1
    return cnt

opt_cnt = 2**32-1
for n in arr:
    if(n % 2 != 0):
        opt_cnt = 0
        break
    res = min_operation(n)
    if (res < opt_cnt) :
       opt_cnt = res

print(opt_cnt)
