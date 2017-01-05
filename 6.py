games = int(raw_input())
for i in range (0,games):
    rows = int(raw_input())
    values = map(int,raw_input().split(' '))
    for j in range(0, rows):
        values[j] = [int(x) for x in '{0:030b}'.format(values[j])]
    sumValues = [0] * 30
    # sumar todas las columnas
    for i in range(0,rows):
        for j in range(0,30):
            sumValues[j] = sumValues[j] + values[i][j]
    # validar par o impar
    isLooser = True
    for i in range(0,30):
         if sumValues[j] % 2 !=0:
             isLooser = False
             break

    if rows % 2 != 0:
        isLooser = not isLooser

    if isLooser :
        print ("L")
    else:
        print ("W")
