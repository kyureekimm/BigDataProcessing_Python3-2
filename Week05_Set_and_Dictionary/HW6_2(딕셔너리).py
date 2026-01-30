contact = {}

while True:

    print("====================")
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    print("--------------------")
    
    select = int(input("메뉴 항목을 선택하시오: "))
    
    if select == 1:
        name = input("이름: ")
        phoneNum = input("전화번호: ")
        contact[name] = phoneNum
        
    elif select == 2:
        name = input("이름: ")
        phoneNum = input("전화번호: ")
        if name in contact:
            del contact[name]
        else:
            print(f"{contact[name]}의 연락처가 없음")
        
    elif select == 3:
        find = input("검색할 이름 입력==> ")
        if find in contact :
            print(f"{find}의 전화번호: {contact[find]}")
        else:
            print(f"{find}의 연락처가 없음")
        
    elif select == 4:
        for name, num in contact.items():
            print(f"{name}의 전화번호: {num}")
    
    else:
        break