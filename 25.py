from collections import deque

g = int(raw_input())

for i in range(0,g):
    n = int(raw_input())
    originList = map(int, raw_input().split(' '))

    orderList = list(originList)
    orderList.sort()
    tempList = []

    validG = 'NO'

    for i in range(2,n):
        tempList = originList
        c = []
        c.append(tempList[i-2])
        c.append(tempList[i-1])
        c.append(tempList[i])

        items = deque(c)

        #rotacion 1
        items.rotate(1)
        tempList[i-2] = items[0]
        tempList[i-1] = items[1]
        tempList[i] = items[2]
        
        if tempList == orderList:
            validG = 'YES'
            break

        #rotacion 2
        items.rotate(1)
        tempList[i-2] = items[0]
        tempList[i-1] = items[1]
        tempList[i] = items[2]
        
        if tempList == orderList:
            validG = 'YES'
            break

        #rotacion 3
        items.rotate(1)
        tempList[i-2] = items[0]
        tempList[i-1] = items[1]
        tempList[i] = items[2]
        
        if tempList == orderList:
            validG = 'YES'
            break

    print validG