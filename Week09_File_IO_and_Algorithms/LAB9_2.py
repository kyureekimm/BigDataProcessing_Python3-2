with open("hello1.txt", "w", encoding="utf8") as f1:
    f1.write("Hello world")
    
with open("hello2.txt", "w", encoding="utf8") as f2:
    f2.write("Hello world\n")
    f2.write("Hello world")
    
    
file_name = input("파일 이름을 입력하세요: ")

with open(file_name, "r") as f:
    content = f.read()
    #print(f.name)
    print(f"파일 안에는 총 {len(content)}개의 글자가 있습니다.")

