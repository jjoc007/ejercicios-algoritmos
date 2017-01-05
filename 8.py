l = int(raw_input())
r = int(raw_input())

maxXor = 0

for i in range(l,r+1):
    for j in range(l,r+1):
        n = i ^ j
        if n > maxXor:
            maxXor = n

print maxXor
