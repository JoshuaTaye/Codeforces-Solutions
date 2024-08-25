def wayTooLongWords(words):
    for i in range(len(words)):
        if len(words[i]) <= 10:
            continue
        first = words[i][0]
        last = words[i][-1]
        length = str(len(words[i]) -2)
        words[i] = ''
        words[i] += first
        words[i] += length
        words[i] += last
    for i in words:
        print(i)

n = int(input())
arr = []
for j in range(n):
    x = input()
    arr.append(x)
wayTooLongWords(arr)
