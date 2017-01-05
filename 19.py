n = int( raw_input())
values =  map(int, raw_input().split(' '))
pasos = 0
posicionActual = 0

while True:
    if posicionActual >= (n-1) :
        break
    else:
        if posicionActual+2 < n and values[posicionActual] == 0 and values[posicionActual+2] == 0:
            pasos = pasos +1
            posicionActual = posicionActual+2
        elif posicionActual+2 < n and values[posicionActual] == 0 and values[posicionActual+2] != 0 and values[posicionActual+1] == 0:
            pasos = pasos +1
            posicionActual = posicionActual+1
        elif posicionActual+2 >= n and posicionActual+1 < n and values[posicionActual] == 0 and values[posicionActual+1] == 0: 
            pasos = pasos +1
            posicionActual = posicionActual+1

print pasos