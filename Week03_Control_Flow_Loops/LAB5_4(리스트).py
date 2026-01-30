num = [100, 96, 209, 22, 30, 117]

for i in range(len(num)):
    if num[i] % 2 == 0 :
        num[i] = num[i] / 10
        
print(num)