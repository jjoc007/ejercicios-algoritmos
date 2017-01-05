parameters = map(int, raw_input().split(" "))

matrix = []

#create matrix
for i in range(1, parameters[0]+1):
    row = []
    for j in range(1, parameters[0]+1):
        row.append([1,1,0,1,0,0,1][(((i*j)**2)  % 7)] == 1)
    matrix.append(row)

diferencias1 = 0
diferencias2 = 0
diferencias3 = 0


for j in range(0,parameters[0]):
    for k in range(0,parameters[0]):
        if matrix[j][k] != matrix[k][parameters[0]-1 - j]:
            diferencias1 = diferencias1 +1

for j in range(0,parameters[0]):
    for k in range(0,parameters[0]):
        if matrix[j][k] != matrix[parameters[0]-1 - j][parameters[0]-1 - k]:
            diferencias2 = diferencias2 +1

for j in range(0,parameters[0]):
    for k in range(0,parameters[0]):
        if matrix[j][k] != matrix[parameters[0]-1 - k][j]:
            diferencias3 = diferencias3 +1

#recorre cada consulta
for i in range(0,parameters[1]):
    side = int(raw_input()) / 90

    if side % 4 == 1:
        print(diferencias1)
    elif side % 4 == 2:
        print(diferencias2)
    elif side % 4 == 3:
        print(diferencias3)
    else:
        print(0)
