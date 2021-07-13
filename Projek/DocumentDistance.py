a = "owasd_asdasD+da9d9as+weoqwpeowq-_dasd**a&dasd"
b = "owasd_asdasD+da9d9as+weoqwpeowq-_dasd**a&dasd"

import re
from math import pi, sqrt,acos

def splitLines(x):
    doc1 = re.split(r'[^a-z0-9A-Z]', x)
    doc2 = [i.lower() for i in doc1 if i != ""]
    print(doc2)
    return doc2

#print(splitLines(a))


def linesToDict(y):
    wordDict = {}

    for j in y:
        if j not in wordDict:
            wordDict[j] = 1
        elif j in wordDict:
            wordDict[j]+=1
    print(wordDict)
    return wordDict
'''
a1 = splitLines(a)
a2 = linesToDict(a1)
print(a2)
'''

def innerProduct(dictA, dictB):
    num = 0
    for word in dictA:
        if word in dictB:
            num += dictA[word]*dictB[word]
    print(num)
    return num

def documentDistance(dictA, dictB):
    num = innerProduct(dictA, dictB)
    print(num)
    denom = sqrt(innerProduct(dictA, dictA)*innerProduct(dictB, dictB))
    print(denom)
    return ((180*acos(num/denom))/pi)


file1 = a
file2 = b
dictA = linesToDict(splitLines(a))
dictB = linesToDict(splitLines(b))
print("Document Distance is", documentDistance(dictA, dictB), "degrees")
print("The Documents is",((90 - documentDistance(dictA, dictB))*100/90), "percent similar")
# 0 Degrees mean the documents is similar 90 degrees mean they very different