import random
daftar = []
def shuffleString(x, n):
    x = str(x)
    n = int(n)
    for _ in range(n):
        gabung = (''.join(random.sample(x, len(x))))
        if gabung not in daftar:
            daftar.append(gabung)
    print(daftar)


shuffleString("aku", 5)