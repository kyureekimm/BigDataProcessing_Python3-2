matrix = [ [3, 5, 2], [7,1,8], [4, 6], [9]]

result = [ pick for one in matrix if sum(one) >= 10 for pick in one ]

print(result)