from collections import deque

parameters = map(int,raw_input().split(' '))
values = raw_input().split(' ')
items = deque(values)
items.rotate(parameters[1])

for a in range(0,parameters[2]) :
    print(items[int(raw_input())])
