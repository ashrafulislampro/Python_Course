arr = input().split()

reverse_word = [word[::-1] for word in arr]
print(" ".join(reverse_word))