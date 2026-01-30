Id = input("아이디: ")
pwd = input("비밀번호: ")

result = ("로그인 성공" if pwd=='1234' else "비밀번호 오류") if Id=='admin' else "아이디 없음"
print(result)