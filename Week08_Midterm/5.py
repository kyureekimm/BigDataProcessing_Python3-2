data = [['홍길동', 85, 78, 92], ['신짱구', 55, 60, 58] , ['최자두', 72, 88, 91]]


PASS = 60
dict = {}
for i in data:
    name = i[0]
    scores = i[1:]
    
    total = sum(scores)
    average = total / len(scores)
    
  
    if average >= PASS:
        result = '합격'
    else:
        result = '불합격'
 
    dict[name] = {
        '점수': scores,
        '총점': total,
        '평균': average,
        '결과': result
    }
    
 
print("학생별 정보:")
print(dict)

