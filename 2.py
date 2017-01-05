import math

parameters = map(int,raw_input().split(' '))
valuesMin  = map(float,raw_input().split(' '))

values = []


for valueMin in valuesMin :
    values.append(int(math.ceil(valueMin / parameters[1] )))

values.sort()

for i in range (1, parameters[0]) :
    if values[i] <= values[ i-1 ] :
        values[i] = values[i-1] + 1

print (sum(values))
