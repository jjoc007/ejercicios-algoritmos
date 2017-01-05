v = raw_input()
n = int(raw_input())
values = raw_input().split(" ")

for i in range(0,n):
    if v == values[i]:
        print(i)
        break
