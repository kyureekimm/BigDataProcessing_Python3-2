name = input('Enter the name: ')
age = int(input(f"Enter the {name}'s age: "))

if age < 10:
    gen = "0대"
elif age >= 50:
    gen = "50대"
else:
    gen = "{}0대".format(age//10)

print(f'이겨울은 {gen}이다')
