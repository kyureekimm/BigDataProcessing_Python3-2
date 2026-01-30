from notebook import Note, NoteBook

def print_menu():
    print("\n---메뉴---")
    print("1: 모든 노트 내용 출력")
    print("2: 특정 노트 내용 출력")
    print("3: 노트 추가(내용이 채워진 노트)")
    print("4: 특정 노트 삭제")
    print("6: 총 페이지 수 출력")
    print("7: 총 글자수 출력")
    print("8: 노트 타이틀 출력")
    print("0: 종료 ")
    print("---------------------------------")

def main():
    my_notebook = NoteBook("명언 노트")
    
    print_menu()

    while True:
        menu = input("메뉴 입력(0이면 종료): ")

        if menu == '1':
            print("<모든 노트 내용 출력>")
            if not my_notebook.notes:
                print("작성된 노트가 없습니다.")
            else:
                for page in sorted(my_notebook.notes.keys()):
                    print(f"{page}페이지 내용 {my_notebook.notes[page]}")

        elif menu == '2':
            print("<노트 내용 출력>")
            try:
                page = int(input("노트 번호 입력: "))
                if page in my_notebook.notes:
                    print(my_notebook.notes[page])
                else:
                    print("해당 페이지에 노트가 없습니다.")
            except ValueError:
                print("숫자만 입력해주세요.")

        elif menu == '3':
            print("<새로운 노트 추가>")
            try:
                page = int(input("노트 번호 입력: "))
                content = input("노트 내용 입력: ")
                new_note = Note(content)
                my_notebook.add_note(new_note, page)
            except ValueError:
                print("페이지 번호는 숫자만 입력해주세요.")
        
        elif menu == '4':
            print("<특정 노트 삭제>")
            try:
                page = int(input("삭제할 노트 번호 입력: "))
                if page in my_notebook.notes:
                    my_notebook.remove_note(page)
                    print(f"{page}페이지의 노트를 삭제했습니다.")
                else:
                    print(f"해당 페이지({page})에 노트가 없습니다.")
            except ValueError:
                print("숫자만 입력해주세요.")

        elif menu == '6':
            print("<모든 페이지 수 출력>")
            print(my_notebook.get_number_of_all_pages())

        elif menu == '7':
            print("<총 글자 수 출력>")
            print(my_notebook.get_number_of_all_characters())

        elif menu == '8':
            print(my_notebook.name)

        elif menu == '0':
            break

        else:
            print("잘못된 메뉴 번호입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()