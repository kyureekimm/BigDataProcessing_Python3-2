import sqlite3

def print_menu():
    print("\n--------------")
    print("1: 테이블 생성")
    print("2: 데이터 전체 조회")
    print("3: id로 데이터 조회")
    print("4: 데이터 입력")
    print("5: 데이터 삭제")
    print("6: 종료")
    print("----------------")

con = sqlite3.connect("naverDB")
cur = con.cursor()

while True:
    print_menu()
    menu = input("메뉴 입력: ")
    
    #테이블 생성
    if menu == '1':
        try:
            sql = "create table student(id char(4), userName char(15), email char(15), birthYear int)"
            cur.execute(sql)
            print("성공: 테이블 생성") 
        except:
            print("오류: 이미 테이블이 있습니다.") 

    #데이터 전체 조회
    elif menu == '2':
        print("사용자ID  사용자이름  이메일  출생연도")
        print("------------------------------------------")
        sql = "SELECT * FROM student"
        cur.execute(sql)
        
        rows = cur.fetchall() 
        for row in rows:
            print("%10s   %10s   %10s   %10d" %(row[0], row[1], row[2], row[3]))

    #ID로 데이터 조회
    elif menu == '3':
        userID = input("사용자ID ==> ")
        
        sql = "SELECT * FROM student WHERE id = '" + userID + "'"
        cur.execute(sql)
        
        print("사용자ID  사용자이름  이메일  출생연도")
        print("------------------------------------------")
        
        rows = cur.fetchall()
        for row in rows:
             print(row[0], row[1], row[2], row[3])
        
    #데이터 입력
    elif menu == '4':
        userID = input("사용자ID ==> ")
        
        sql_check = "SELECT * FROM student WHERE id = '" + userID + "'"
        cur.execute(sql_check)
        row = cur.fetchone() 
        
        if row != None: 
            print("오류: 데이터 입력 오류가 발생함 (ID 중복)")  
        else:
            userName = input("사용자이름 ==> ")
            userEmail = input("이메일 ==> ")
            userBday = input("출생연도 ==> ")
            
            sql = "INSERT INTO student VALUES('" + userID + "', '" + userName + "', '" + userEmail + "', " + userBday + ")"
            cur.execute(sql)
            con.commit() 
            print("성공: 데이터 입력") 

    #데이터 삭제
    elif menu == '5':
        userID = input("삭제할 id를 입력: ")
        sql = "DELETE FROM student where id = '" + userID + "'"
        cur.execute(sql)
        con.commit() 
        print("성공: 데이터 삭제")

    #종료
    elif menu == '6':
        break

con.close()