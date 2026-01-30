with open("hello2.txt", "w", encoding="utf8") as f:
    f.write("Hello world\n")
    f.write("Hello world\n")
    

input_file = input("입력파일 이름 입력: ")
output_file = input("출력파일 이름 입력: ")
delete_string = input("삭제할 문자열을 입력: ")

with open(input_file, "r") as f:
    content = f.read()
    #print(content)
    new_content = content.replace(delete_string, "")


with open(output_file, "w", encoding="utf8") as f_out:
    f_out.write(new_content)
    