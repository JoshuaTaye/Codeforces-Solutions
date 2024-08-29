def calculateFunction(x):
    if x % 2 == 0:
        return int(x/2)
    else:
        return int((x+1)/2 * -1)

x = int(input())
print(calculateFunction(x))

