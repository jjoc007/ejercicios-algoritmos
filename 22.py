parameters = map(int, raw_input().split(' '))
toys = map(int, raw_input().split(' '))
toys.sort()

amountToys = 0
price = 0

for i in range(0, parameters[0]):
    price = price + toys[i]

    if price == parameters[1]:
        amountToys = amountToys +1
        break
    elif price > parameters[1]:
        break
    else:
        amountToys = amountToys +1

print amountToys





