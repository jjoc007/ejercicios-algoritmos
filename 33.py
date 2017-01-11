#xor con for
#https://www.hackerrank.com/contests/w28/challenges/the-great-xor
g =  int(raw_input())
for i in range(0,g):
    x = int(raw_input())
    cont = 0
    for j in range(0,x):
        if j ^ x > x :
            cont =  cont+1
    print cont


