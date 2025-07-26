def sum(a, b = 0, c = 0):
    result = a + b
    return result
    
    
# total = sum(3, 4, 8)  # This will return 7
# print(total)  # This will print 7


#args or Tuple
def sum_all(a, b, *args):
    print("args = ", args)
    sums = 0
    for num in args:
        print(num)
        sums += num
    # print("sums = ", sums)
    return sums
    
total1 = sum_all(3, 4, 8, 5, 9)  # This will print (3, 4, 8)
print("result = ", total1)  # This will print None since sum_all does not return anything



