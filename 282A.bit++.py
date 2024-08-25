def bitPlus (bits):
    x = 0
    for i in bits:
        if '++' in i:
            x += 1
        if '--' in i:
            x -= 1
    return x

n = int(input())
arr = []
for j in range(n):
    y = input()
    arr.append(y)
print(bitPlus(arr))