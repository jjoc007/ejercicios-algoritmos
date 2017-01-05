import math

s = raw_input().strip()
n = long(raw_input().strip())

oc = 0

cadFinal = ''
if "a" not in s:
    oc = 0
elif len(s) == 1:
    oc = n
elif n > len(s):
    nRepeat = math.ceil(float(n) / float(len(s)))
    nRepeat = int(nRepeat)

    for i in range(0,nRepeat):
        cadFinal = cadFinal+s

    cadFinal = cadFinal[0:n]
    oc = cadFinal.count('a')

else:
     cadFinal = s[0:n]
     oc = cadFinal.count('a')

print(oc)
