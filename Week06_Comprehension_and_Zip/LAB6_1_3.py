num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))
num3 = int(input("세 번째 정수를 입력하세요: "))

largest_num = 0

if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
else:
    largest_num = num3

print(f"가장 큰 수는 {largest_num} 입니다.")