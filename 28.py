g =  int(raw_input())


for i in range(0,g):
    parameters = map(int, raw_input().split(' '))
    
    mat = []
    for j in range(0, parameters[0]):
        mat.append(raw_input())
    
    parametersMatS = map(int, raw_input().split(' '))

    matS = []
    for j in range(0, parametersMatS[0]):
        matS.append(raw_input())

    print mat
    print 'buscar'
    print matS
