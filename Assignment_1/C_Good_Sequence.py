number = int(input())
arr = list(map(int, input().split()))


num_cnt = {}
for num in arr:
    if num in num_cnt:
        num_cnt[num] += 1
    else:
        num_cnt[num] = 1
    
cnt = 0
for item in num_cnt:
   
   
    if item > num_cnt[item]:
        cnt += num_cnt[item]
    if item < num_cnt[item]:
        cnt += (num_cnt[item] - item)
    
print(cnt)