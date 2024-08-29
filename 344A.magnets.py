def magnets(arr):
    group = 1
    for i in range(len(arr)-1):
        if arr[i][1] == arr[i+1][0]:
            group += 1
    return group



n = int(input())
ar = []
for i in range(n):
    ar.append(input())
print(magnets(ar))