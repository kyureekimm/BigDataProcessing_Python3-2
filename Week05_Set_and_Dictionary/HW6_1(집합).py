list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 60, 70, 80]

set1 = set(list1)
set2 = set(list2)

print(f"집합 A {set1}")
print(f"집합 B {set2}")

union = set1 | set2

intersection = set1 & set2

result = union - intersection

print(f"어느 한쪽에만 있는 요소들 {result}")


