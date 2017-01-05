n = int(raw_input())
array = map(int, raw_input().split())
arraySet = set(array)

maxSum = 0

for i in range (0, len(arraySet)):
    value = list(arraySet)[i]
    if array.count(value) > maxSum:
        maxSum = array.count(value)

print(str(n-maxSum))
