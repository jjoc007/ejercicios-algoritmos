#rotacion de elementos en una lista
#algoritmo para rotar una matriz por capas n veces

from collections import deque

parameters =  map(int, raw_input().split(' '))
m = parameters[0]
n = parameters[1]
k = parameters[2]
s = 0
l = 0
mT = parameters[0]
nT = parameters[1]

matriz = []
rings = []
temp = []

for i in range(0,m):
    matriz.append(map(int, raw_input().split(' ')))

while s < mT and l < nT:
    ring = []

    #copy the first row from the remaining rows
    for i in range(l, nT):
        ring.append(matriz[s][i])
    
    s = s + 1

    #copy the last column from the remaining columns
    for i in range(s, mT):
        ring.append(matriz[i][nT-1])
    
    nT = nT - 1

    #copy the last row from the remaining rows
    if s < mT:
        for i in range(nT-1, l-1, -1):
            ring.append(matriz[mT-1][i])
        mT = mT - 1

    #copy the first column from the remaining columns
    if l < nT:
        for i in range(mT-1, s-1, -1):
            ring.append(matriz[i][l])
        l = l +1 

    rings.append(ring)

#rotating rings
for i in range(0,len(rings)):
    items = deque(rings[i])
    items.rotate((-1)*k)
    temp.extend(items)

s = 0
l = 0
mT = parameters[0]
nT = parameters[1]
indexTemp = 0

while s < mT and l < nT:
    ring = []

    #copy the first row from the remaining rows
    for i in range(l, nT):
        matriz[s][i] = temp[indexTemp]
        indexTemp += 1
    
    s = s + 1

    #copy the last column from the remaining columns
    for i in range(s, mT):
        matriz[i][nT-1] = temp[indexTemp]
        indexTemp += 1
    
    nT = nT - 1

    #copy the last row from the remaining rows
    if s < mT:
        for i in range(nT-1, l-1, -1):
            matriz[mT-1][i] = temp[indexTemp]
            indexTemp += 1
    
        mT = mT - 1

    #copy the first column from the remaining columns
    if l < nT:
        for i in range(mT-1, s-1, -1):
            matriz[i][l] = temp[indexTemp]
            indexTemp += 1
        l = l +1 

for i in range(0,m):
    print ' '.join(map(str, matriz[i]))
