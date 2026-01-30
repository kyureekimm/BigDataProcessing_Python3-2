text = input("문자열 입력 ==>")

save = {}		//save = dict()

for x in text:
    save[x] = save.get(x, 0) + 1
    
    
print(f"문자들의 빈도수 = {save}")