def teams(sure):
    total = 0
    for i in range(len(sure)):
        summ = 0
        sure[i] = sure[i].split(" ")
        for k in (sure[i]):
           summ += int(k)
        if summ > 1:
            total += 1
    return total


n = int(input())
arr = []
for j in range(n):
    x = input()
    arr.append(x)
print(teams(arr))