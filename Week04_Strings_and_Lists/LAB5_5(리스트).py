numList = []

while True:
    num = int(input("수를 입력하시오(-1이면 입력 끝): "))
    
    if num == -1:
        break
    
    numList.append(num)
    
find = int(input("찾고 싶은 값을 입력하시오: "))
print(f"찾는 값의 위치: {numList.index(find)}")

    