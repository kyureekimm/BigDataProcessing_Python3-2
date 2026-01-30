def movie_fee(day, *age):
    cnt = 0   
    total = 0  
    
    for i in age:
        
       
        ticket = 12000
        
        if i <= 13:  
            cnt += 1
            ticket = 12000 * 0.5   
        elif i >= 65:   
            cnt += 1
            ticket = 12000 * 0.7   
         

        if day == '수':
            ticket = ticket * 0.9   
        
 
        total += ticket
        
    return (total, cnt)
 


result = []
result.append( movie_fee("수", 10, 20, 70) )
result.append( movie_fee("월", 10, 20, 70) )
result.append( movie_fee("수", 10, 20, 70, 34, 65) )

 

for res in result:
    total_fee = res[0]
    discount_count = res[1]
    
    print(f"-요금: {total_fee}원")
    print(f"할인적용 인원 수: {discount_count}명")
