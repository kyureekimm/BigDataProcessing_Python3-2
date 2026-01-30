stock = { '커피' : 15,
          '펜' : 3,
          '종이컵' : 20,
          '콜라' : 7,
          '라면' : 20
          }

print(f'판매 전 재고: {stock}', end='\n\n')
sold = input("판매한 상품을 입력하시오: ")

print()



stock[sold] = stock[sold] - 1


print(f'판매 후 재고: {stock}', end='\n\n')