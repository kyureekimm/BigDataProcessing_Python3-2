num = [100, 96, 209, 22, 30, 117]

num_copy = num[:]

for x in num_copy:
    if x%2==0:
        idx = num_copy.index(x)
        num[idx] /= 10
        
print(num)