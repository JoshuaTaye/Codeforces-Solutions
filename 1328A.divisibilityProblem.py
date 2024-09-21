def divisibilityProblem(ar):
    res = []
    for i in ar:
        step = i[0] % i[1]
        if step == 0:
            res.append(0)
        else:
            res.append(i[1] - step)
    for k in res:
        print(k)
n = int(input())
arr = []
for j in range(n):
    arr.append(list(map(int, input().split())))
divisibilityProblem(arr)