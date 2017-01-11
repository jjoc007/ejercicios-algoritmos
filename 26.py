g = int(raw_input())

for i in range(0,g):
    parameters =  map(int, raw_input().split(' '))

    indexPoisoned = (parameters[2]-1) + parameters[1]

    if indexPoisoned <= parameters[0]:
        print indexPoisoned
    else:
        mod  = parameters[1] % parameters[0]
        indexPoisoned = (mod) + (parameters[2]-1)
        print indexPoisoned
        
