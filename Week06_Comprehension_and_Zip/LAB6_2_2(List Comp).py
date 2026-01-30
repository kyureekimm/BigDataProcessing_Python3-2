'''
result = [i*i for i in range(1,10) if i%2==0 ]

for r in result:
    print(r)
'''

result = []
for i in range(1, 10):
    if i % 2 == 0:
        print(i*i)