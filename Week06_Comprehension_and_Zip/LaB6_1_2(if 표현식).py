year = int(input("년도를 입력하세요: "))
result = "윤년입니다" if (year%4==0 and year%100!=0) or (year%400==0) else "윤년이 아닙니다"
print(result)