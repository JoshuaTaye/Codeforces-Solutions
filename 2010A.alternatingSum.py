def alternatingSum(arr):
    for i in range(len(arr)):
        summ = 0
        multi = 1
        for j in arr[i]:
            summ += multi * j
            multi *= -1
        print(summ)

n = int(input())
ar = []
for k in range(n):
    x = int(input())
    ar.append(list(map(int, input().split())))
alternatingSum(ar)