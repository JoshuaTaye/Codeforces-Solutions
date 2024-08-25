def wrongSubtraction(a,b):
    while b > 0:
        if a % 10 == 0:
            a /= 10
            b -= 1
        else:
            a -= 1
            b -= 1
    return int(a)

n = input()
n = n.split(" ")
print(wrongSubtraction(int(n[0]),int(n[1])))
