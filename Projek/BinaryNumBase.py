def NumToBinary(number):
    n = 0

    while True :
        if 2**n < number :
            n += 1
        elif 2**n == number:
            break
        elif 2**n > number :
            n -= 1
            break
        continue
    
    binary = []

    while True:
        if n < 0:
            break
        elif number < 2**n:
            binary.append("0")
            n -= 1
        elif number >= 2**n :
            number -= 2**n
            binary.append("1")
            n -= 1
        continue
   
    code = "".join(binary)

    print(code)

def BinaryToNum(binary):
    binary = list(str(binary))
    num = 0

    for i in range(len(binary)):
        if binary[i] != "1" and binary[i] != "0":
            return "This isn't Binary"
        else :
            if binary[i] == "1":
                num += 2**(len(binary) - 1 - i)
            else :
                pass
    return num   
    
    

NumToBinary(8)
print(BinaryToNum(1010))
