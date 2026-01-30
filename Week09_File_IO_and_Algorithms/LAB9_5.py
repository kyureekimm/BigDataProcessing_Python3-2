data = [20, 10, 40, 30, 50]
with open("num.txt", "w", encoding="utf8") as f:
    for i in data:
        f.write(str(i) + "\n")
        
total = 0
count = 0
infile = open("num.txt", "r")
for i in infile:
    total += float(i)
    count += 1

infile.close()

average = total / count

outfile = open("num.txt", "a")
outfile.write(f"합은 {total}\n")
outfile.write(f"평은 {average}")

outfile.close()