Alen = 33; Acnt = 30; Aprice = 13550
Blen = 35; Bcnt = 24; Bprice = 15960
Clen = 30; Ccnt = 33; Cprice = 11990

A = Aprice / (Alen * Acnt)
B = Bprice / (Blen * Bcnt)
C = Cprice / (Clen * Ccnt)


if A < B and A < C:
    print("A_market이 1m당 {A:.2f}으로 최저가이다")
elif B < A and B < C:
    print("B_market이 1m당 {:.2f}으로 최저가이다".format(B))
else:
    print("C_market이 1m당 {:.2f}으로 최저가이다".format(C))
