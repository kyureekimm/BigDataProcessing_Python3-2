answer = 88
print('숫자를 맞혀 보세요. (1~100) ')
guess = int(input())

while answer != guess:
    if guess < answer :
        print('숫자가 너무 작아.')
    else:
        print('숫자가 너무 큽니다.')
    guess = int(input())
else:
    print(f'정답입니다. 입력한 숫자는 {answer}입니다.')
