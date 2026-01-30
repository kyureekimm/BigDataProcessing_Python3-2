import sqlite3

con = sqlite3.connect("naverDB")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS countTable")
cur.execute("CREATE TABLE countTable(one_char char(4), count int)")

text = """죽는 날까지 하늘을 우러러 한 점 부끄럼이 없기를,
잎새에 이는 바람에도 나는 괴로워했다.
별을 노래하는 마음으로 모든 죽어가는 것을 사랑해야지.
그리고 나한테 주어진 길을 걸어가야겠다.
오늘 밤에도 별이 바람에 스치운다."""

print("원문")
print(text)
print("\n-------------------------")
print("문자   빈도수")
print("-------------------------")


count_dic = {}
for ch in text:
    if ('가' <= ch <= '힣') or ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        if ch in count_dic:
            count_dic[ch] += 1
        else:
            count_dic[ch] = 1

for char, count in count_dic.items():
    sql = "INSERT INTO countTable VALUES('" + char + "', " + str(count) + ")"
    cur.execute(sql)

con.commit()

sql = "SELECT * FROM countTable ORDER BY count DESC"
cur.execute(sql)

rows = cur.fetchall()
for row in rows:
    print(row[0], "   ", row[1])

con.close()

