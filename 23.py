parameters = map(int, raw_input().split(' '))
values = map(int, raw_input().split(' '))
values.sort(reverse=True)

print 'listo'

pairs = 0


for i in range(0, parameters[0]-1):
    for j in range(1,parameters[0]):
        if(values[i] - values[j] == parameters[1]):
            pairs = pairs+1

print pairs
