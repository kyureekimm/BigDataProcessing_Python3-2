data = input("정수를 공백으로 구분하여 입력: ")

new = data.split()
 
result = list(set(new))
 
intdata = [ int(i) for i in result]
intdata.sort()

print(intdata)
