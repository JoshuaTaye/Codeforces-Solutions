def georgeAndAccommodation(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i][1] - arr[i][0] >= 2:
            count += 1
    return count

n = int(input())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))
print(georgeAndAccommodation(ar))