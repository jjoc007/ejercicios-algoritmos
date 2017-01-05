caracteres =  int(raw_input())
cadena = raw_input()
listaCaracteresSinRepetir = list(set(list(cadena)))

listaCaracteresDes = []

lenMax = 0

def  validarCadena(cad):
    listCar = list(set(cad))
    isValid = True
    if len(listCar) == 2:

        car0 = ''
        car1 = ''

        if listCar[0] == cad[0]:
            car0 = listCar[0]
            car1 = listCar[1]
        else:
            car1 = listCar[0]
            car0 = listCar[1]

        for i in range(0,len(cad)):
            if (i%2 == 0 and cad[i] == car1) or (i%2 == 1 and cad[i] == car0):

                isValid = False
                break

        if isValid:

            return len(cad)


for i in range(0,len(listaCaracteresSinRepetir)):
    for j in range(i+1,len(listaCaracteresSinRepetir)):
        listaCaracteresDescartar = list(listaCaracteresSinRepetir)
        listaCaracteresDescartar.remove(listaCaracteresSinRepetir[i])
        listaCaracteresDescartar.remove(listaCaracteresSinRepetir[j])

        listaCaracteresDes.append(listaCaracteresDescartar)

for i in range(0, len(listaCaracteresDes)):
    cadAux =  cadena
    for j in range(0,len(listaCaracteresDes[i])):
        cadAux = cadAux.replace(listaCaracteresDes[i][j],'')
    lenVal = validarCadena(cadAux)

    if lenVal > lenMax:
        lenMax = lenVal


print(lenMax)
