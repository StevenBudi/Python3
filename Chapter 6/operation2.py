from main import *

a = 2
b = 3
c = 5
d = 7
e = 17

print(a, '+', a*2, '*',a*3, '-', a*2, '=', add(a,a*2)*subs(a*3,a*2)) 
print('(4 +  7)', '*', '(6 - 9)', '=', add(a*2,d)*subs(a*b,b*b))
print('(10 + 2)', '/', '(7 + 5)', '/', '(12 -34)', '=', add(c*a,a)/add(d,c)/subs(c+d,e*2))


