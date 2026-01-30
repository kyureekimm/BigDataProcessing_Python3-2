s = input("입력 텍스트: ")

s_split = s.split()

set1 = set(s_split)

print(f"사용된 단어의 종류= {set1}")
print(f'사용된 단어의 개수= {len(set1)}')