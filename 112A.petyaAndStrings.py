def petyaAndStrings(a, b):
    a = a.lower()
    b = b.lower()
    if a > b:
        return 1
    if b > a:
        return -1
    return 0

n = input()
x = input()
print(petyaAndStrings(n, x))