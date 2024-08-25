def wordCapitalization(word):
    new = ''
    new += word[0].upper()
    for i in range(1, len(word)):
        new += word[i]
    return new


n = input()
print(wordCapitalization(n))