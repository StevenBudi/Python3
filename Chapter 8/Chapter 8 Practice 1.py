#Chapter 8 Praktikum 1
#no. 1
a = [1, 5, 6, 3, 9, 11, 20]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#no. 2
a.insert(3, 10)
b.insert(2, 15)
#no. 3
a.append(4)
b.append(8)

#no. 4
a.sort()
b.sort()

#no. 5
c = a[:7]
d = b[2:9]

#no 6
e = c.copy()
for i in range(len(d)):
    e[i] += d[i]
print(e)

#no. 7
def convert(e):
    return tuple(e)
print(convert(e))

#no. 8
print(max(convert(e)))
print(min(convert(e)))
print(sum(convert(e)))

#no. 9
myString = "python is a fun programming language"

#no. 10
ordered  = set(myString)
print(ordered)

#no. 11
def change(ordered):
    return list(ordered)

l = change(ordered)
sortedStr = l.sort()
print(l)

