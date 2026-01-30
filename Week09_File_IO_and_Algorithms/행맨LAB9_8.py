import random
words = [ "woodz", "marryme" ]
answer = random.choice(words).strip()

life = len(answer) + 2
guesses = []
is_win = False

while life > 0 :
    
    result = ""
    for char in answer:
        if char in guesses:
            result += char
        else:
            result += "*"
            
    print(result)
    print()
    
    if result == answer:
        print("사용자 승리 ㅋㅋㅋ")
        is_win = True
        break
        
        
    
    guess = input("단어를 추측하시오: ")
    guesses.append(guess)
    
    if guess in answer:
        life = life
    else:
        life -= 1
        print(f"틀렸음! {life}번 기회 남음") 
        
        
if is_win == False:
    print(f"사용자 패배! 정답은 {answer}")


'''
import random

word_list = [
    "blood\n",
    "off\n"
]
with open("words.txt", "w", encoding="utf8") as f:
    f.writelines(word_list)


with open("words.txt", "r", encoding="utf8") as f:
    words = f.readlines() 
    
answer = random.choice(words).strip()
    
life = len(answer) + 2 
guesses = [] 
is_win = False

while life > 0:

    current_board = ""
    all_correct = True 
    
    for char in answer: 
        if char in guesses: 
            current_board += char 
        else:
            current_board += "*" 
            all_correct = False

    if all_correct == True: 
        print(current_board) 
        print("사용자 승리 …")
        is_win = True
        break 

    print(current_board)
    print()

    guess = input("단어를 추측하시오: ")

    if len(guess) != 1 or not guess.isalpha():
        print("한 개의 알파벳만 입력하세요!")
        continue 
    
    if guess in guesses: 
        print("이미 추측한 글자입니다.")
        continue 

    guesses.append(guess)

    if guess in answer: 
        life -= 1
    else:
        life -= 1 
        print(f"틀렸음! {life} 기회가 남았음!")
        
if is_win == False: 
    print(f"사용자 패배!! 정답은 {answer}")
'''