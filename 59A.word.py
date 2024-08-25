def word(w):
    isUpperCount = 0
    isLowerCount = 0
    for i in w:
        if i.isupper():
            isUpperCount += 1
        else:
            isLowerCount += 1
    if isUpperCount > isLowerCount:
        return w.upper()
    return w.lower()

n = input()
print(word(n))