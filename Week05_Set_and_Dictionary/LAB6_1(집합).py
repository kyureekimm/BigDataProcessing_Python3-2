s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")

s1_lower = s1.lower()
s2_lower = s2.lower()

s1_list = s1_lower.split()
s2_list = s2_lower.split()

set1 = set(s1_list)
set2 = set(s2_list)

intersection = set1.intersection(set2)

if len(set2) == 0:
    ans = 0.0
else :
    ans = (len(intersection) / len(set2)) * 100


print(f"표절률 = {ans}")