cadena =  list(raw_input())

while True:

    repetidos = False

    #recorre cadena para encontrar caracteres repetidos
    for  i in range(1, len(cadena)):
        if cadena[i] == cadena[i-1]:
            del cadena[i]
            del cadena[i-1]
            repetidos = True
            break

    if not repetidos:
        break

if len(cadena) == 0:
    print('Empty String')
else:
    print(''.join(cadena))
