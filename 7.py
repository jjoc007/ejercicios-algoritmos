limitsHouse =  map(int, raw_input().split(" "))
positionsTrees = map(int, raw_input().split(" "))
ammountFruits = map(int, raw_input().split(" "))
apples = map(int, raw_input().split(" "))
oranges =  map(int, raw_input().split(" "))

nApples = 0
nOranges = 0

#find aples
for i in range(0,ammountFruits[0]):
    if  limitsHouse[0] <= (positionsTrees[0]+apples[i]) <= limitsHouse[1] :
        nApples = nApples +1

#find oranges
for i in range(0,ammountFruits[1]):
    if  limitsHouse[0] <= (positionsTrees[1]+oranges[i]) <= limitsHouse[1] :
        nOranges = nOranges +1

print(nApples)
print(nOranges)
