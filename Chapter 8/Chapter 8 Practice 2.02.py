#no. 2
import statistics

def data(*x):
    x = list(x)
    a = statistics.mean(x)
    b = max(x)
    c = min(x)
    d = [a, b, c]
    print(x)
    print(d)

data(1, 2, 3, 4)