data = [5.0, 4.3, 1.7, 6.7, 2.1]
with open("data.txt", "w", encoding="utf8") as f:
    for i in data:
        f.write(str(i) + "\n")
   

input_name = input("입력파일 이름: ")
output_name = input("출력파일 이름: ")

total = 0.0
count = 0
with open(input_name, "r") as f:
    for line in f:
        total += float(line)
        count += 1
        
average = total / count

with open(output_name, "w", encoding="utf8") as f_out:
    f_out.write(f"합계 = {total}\n")
    f_out.write(f"평균 = {average:.2f}\n")
    
with open(output_name, "r", encoding="utf8") as f_out:
    result = f_out.read()
    print(result)