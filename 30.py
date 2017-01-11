# recorre items de 3 por incrementos de 1
# https://www.hackerrank.com/challenges/beautiful-binary-string

lenBin =  int(raw_input())
values =  list(raw_input())

cont = 0

for i in range(2,lenBin):
    if values[i-2] == '0' and values[i-1] == '1' and values[i] == '0':
        values[i] = 1
        cont =  cont + 1

print cont