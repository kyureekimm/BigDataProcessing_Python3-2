student_score = { "홍길동" : [99, 83, 95],
                  "신짱구" : [68, 45, 78],
                  "최자두" : [25, 56, 69]
                  }

for name, scores in student_score.items():
    total = sum(scores)
    average = total / len(scores)
    
    print(f"{name}의 점수 = {scores}")
    print(f"{name}의 평균성적 = {average:.2f}")
    print('-' * 25)