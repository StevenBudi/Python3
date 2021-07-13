'''
odds = 0
total = 0
for i in range(100):
    if i % 2 != 0:
        print(i)
        total += 1
        odds += i
    else :
        pass
'''
oddsNum = [i for i in range(101) if i % 2 != 0]
print(*oddsNum, sep="\n")
print("Odd Numbers Total {}".format(sum(oddsNum)))
print("Odds Number Count {}".format(len(oddsNum)))
        

