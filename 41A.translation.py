def translate(x , y):
    if len(x) != len(y):
        return "NO"
    j = 0
    for i in range(len(x)-1, -1, -1):
        if x[i] == y[j]:
            j += 1
            continue
        else:
            return "NO"
    return "YES"


a = input()
b = input()
print(translate(a, b))