money = 32892700

A = money%100000
money_1 = (money - A)//100000
print(money_1)

B = A%50000
money_2 = (A - B)//50000
print(money_2)

C = B%10000
money_3 =  (B -C)//10000
print(money_3)

D = C%5000
money_4 = (C-D)//5000
print(money_4)

E = D%500
money_5 = (D - E)//500
print(money_5)

F = E%100
money_6 = (E - F)//100
print(money_6)