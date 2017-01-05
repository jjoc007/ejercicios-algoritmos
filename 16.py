q =  int(raw_input())
valoresTripletes = []



def findTriplete():

    for conjunto in valoresTripletes:
        if conjunto[0][0] == r and conjunto[0][1] == r2 and  conjunto[0][2] == r3:
            return conjunto[1][0], conjunto[1][1], conjunto[1][2]

    #definir limites maximos
    maxR = r+r2+r3
    lim = 0
    for i in range(0,1000):
        if maxR <= ((i**2)+(i**3)+(i**4)):
            lim = i
            print lim
            break

    for i in range(0,lim+1):
        for j in range(0,lim+1):
            for k in range(0,lim+1):
                if (r == ((i**2) + (j ** 2) + (k**2) )) and (r2 == ((i**3) + (j ** 3) + (k**3) )) and (r3 == ((i**4) + (j ** 4) + (k**4) )):
                    valores = [r,r2,r3]
                    triplete = [i,j,k]
                    conjunto = [valores,triplete]
                    valoresTripletes.append(conjunto)
                    return i,j,k

    
def findS():
    res = 0
    for i in range(l,rr+1):
        res = res + ((a**i)+(b**i)+(c**i))
    return res % ((10**9)+7)

for query in range(0,q):
    parameters =  map(int,raw_input().split(' '))

    a  = 0
    b  = 0
    c  = 0
    r  = parameters[0]
    r2  = parameters[1]
    r3  = parameters[2]
    pot  = 2
    pot2 = 3
    pot3 = 4
    l=parameters[3]
    rr =parameters[4]

    a,b,c = findTriplete()
    res = findS()

    print(res)




