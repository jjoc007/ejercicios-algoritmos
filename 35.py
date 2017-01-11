#subsequences - subsecuencias de un array
# https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight
lenPrin = int(raw_input())
numPrin = map(int,list(raw_input()))


def printSubsequences():
    arr = [1,2,3,4]
    n = 4
    p = 2 ** lenPrin
    s = ''
    res = 0

    for counter in range(1,p):
        for j in range(0,lenPrin):
            if counter & (1<<j):
                s = s + str(numPrin[j])
        
        num = long(s)
        if num % 8 == 0:
            res = res +1
        s = ''
    
    return res


cont = printSubsequences()

print(str(cont % ((10**9)+7)))