sentence = "You said some winds blow forever and I didn't understand"
rem = ["some", "forever"]

word_list = sentence.split()

for word in rem :
    word_list.remove(word)

print(f"원본 문자열:{sentence}")
print(f"삭제 단어들:{rem}")
print(f"삭제 후 남은 단어들:{word_list}")