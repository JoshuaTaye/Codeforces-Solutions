def tram(stops):
    curr = 0
    maxx = curr
    for i in stops:
        curr -= int(i[0])
        curr += int(i[1])
        if curr > maxx:
            maxx = curr
    return maxx

n = int(input())
arr = []
for j in range(n):
    x = input().split()
    arr.append(x)
print(tram(arr))

