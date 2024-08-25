def bearAndBigBrother(w):
    x = int(w[0])
    y = int(w[1])
    i = 0
    while y >= x:
        y *= 2
        x *= 3
        i += 1
    return i

n = input()
n = n.split(" ")
print(bearAndBigBrother(n))