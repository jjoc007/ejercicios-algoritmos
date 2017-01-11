#alternar valores A y B 
# https://www.hackerrank.com/challenges/alternating-characters

g =  int(raw_input())

for i in range(0,g):
    values = list(raw_input())
    cont = 0
    #impar A, par B
    alternador = 1 

    for j in range(0,len(values)):

        if j == 0:
            if values[j] == 'A':
                alternador = 2
            else:
                alternador = 1

        else:
            if alternador % 2 == 0:
                if values[j] == 'B':
                    alternador = alternador + 1
                else:
                    cont = cont +1
            else:
                if values[j] == 'A':
                    alternador = alternador + 1
                else:
                    cont = cont +1

    print cont
