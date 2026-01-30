
num = 10
binary_str = ''
while num > 0:
    r = num % 2
    num //= 2
    binary_str = str(r) + binary_str
    
    
print(binary_str)