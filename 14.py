
n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

def getCaracter(c):
    numberC = ord(c)

    for i in range(0,k):
        if numberC == 122:
            numberC =97
        elif numberC == 90:
            numberC = 65
        elif (numberC > 96 and numberC < 122) or (numberC > 64 and numberC < 91):
            numberC = numberC +1

    return chr(numberC)

cadFinal = ''
for i in range(0,n):
    caracter = getCaracter(s[i])
    cadFinal = cadFinal+caracter

print cadFinal
