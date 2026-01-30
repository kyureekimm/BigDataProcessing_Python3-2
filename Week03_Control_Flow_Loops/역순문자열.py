sentence = input('sentence = ')


'''
for i in range (len(sentence) -1, -1, -1):
    print(sentence[i], end='')
'''    
 

''' (1)이건 c언어 스타일
for i in range(len(sentence)):
    print(senetence[len(sentece)-1-i])
'''



reverse_str = ''
for ch in sentence:
    reverse_str = ch + reverse_str

print(reverse_str)
