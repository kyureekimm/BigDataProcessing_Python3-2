names = ['신짱구', '김철수', '유리', '맹구']
pythons =[100, 90,60, 90]
java = [90,98, 70, 80]
c = [97, 89, 60, 91]

result = []
for n, p, j, c in zip(names, pythons, java, c):
    result.append((n, p+j+c, (p+j+c)/3))
    
    
print(result)