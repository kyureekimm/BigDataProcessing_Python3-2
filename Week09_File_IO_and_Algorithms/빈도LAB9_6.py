with open("LAB9_6.txt", "w", encoding="utf8") as f:
    f.write("Twinkle, twinkle, little star How I wonder whatyou are Up above the world so high Like a diamond in the sky Twinkle, twinkle little star How Iwonder what you are When the blazing sun is gone When he nothing shines upon Then you show your little light Twinkle, twinkle, all the night Twinkle, twinkle, little star How I wonder what you are")

infile = open("LAB9_6.txt", "r")

search_word = input("단어 입력: ")

word_dic = {}

for line in infile:
    words = line.split()
    
    for word in words:
        clean_word = word.replace(",", "").lower()
    
        word_dic[clean_word] = word_dic.get(clean_word, 0) + 1

infile.close()

count = word_dic.get(search_word, 0)
print(f"{search_word} 빈도: {count} ")

