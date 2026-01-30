def f(text):
    reverse_str = ''
    for ch in text:
        reverse_str = ch + reverse_str
        
    pick = ''

    if text == reverse_str:
        pick = 'YES'
    else:
        pick = 'NO'
    
    print(f"원문자열: {text}, 역순: {reverse_str}, 회문여부: {pick}")


 
text_list = []
for i in range(1, 6):
    text = input(f"{i}번째 문자열 입력: ")
    text_list.append(text)


print()
for text in text_list:
    f(text)