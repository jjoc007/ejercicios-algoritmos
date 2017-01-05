potencias = []

for i in range(0,65):
    potencias.append(2**i)

games = int(raw_input())

for i in range(0,games):
    n = int(raw_input())
    jugador = 0 # par es Louise; impar es Richard

    while(True):
        #valdiar si es potencia perfecta de 2
        if n in potencias:
            print "numero potencia 2: "+str(n)
            n = n / 2
            print "numero potencia dividido en 2: "+str(n)
        else:

            for j in range(1,65):
                if potencias[j-1] <= n < potencias[j]:
                    print "numero potencia 2 (FOR )"+str(potencias[j-1])

                    n = potencias[j-1]

                    print "numero potencia 2 /2 (FOR )"+str(n)

                    break

        if n == 1:
            break
        else:
            jugador = jugador +1

    if jugador % 2 == 0:
        print("Louise")
    else:
        print("Richard")
