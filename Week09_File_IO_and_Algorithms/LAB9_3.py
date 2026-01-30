num = int(input("정수를 입력하시오: "))       

with open("output1.txt", "w", encoding="utf8") as f:
    f.write(str(num) + ": ")
    
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
            f.write(str(i) + " ")
            
print()
    
print(f"출력파일: output1.txt")
with open("output1.txt", "r") as f:
    content = f.read()
    print(content)
        
