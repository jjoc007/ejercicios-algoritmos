n =  int(raw_input())
values =  map(int,raw_input().split(' '))
valMin = min(values)
ocurrences = values.count(valMin)

print(str((valMin*2)/ocurrences)+' '+str(ocurrences))
