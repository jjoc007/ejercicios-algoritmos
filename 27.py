#eliminar duplicados
# interseccion entre varias listas

rocks = int(raw_input())
res = 0
listRocks = []


for i in range(0,rocks):
    values = list(raw_input())
    listRocks.append(list(set(values)))

#interseccion entre conjuntos
inter =  list(set.intersection(*map(set, listRocks)))

print len(inter)