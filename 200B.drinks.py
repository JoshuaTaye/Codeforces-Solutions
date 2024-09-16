def drinks(arr, n):
    summ = 0
    for i in arr:
        summ += i
    return summ/n

nn = int(input())
ar = list(map(int, input().split()))
print(drinks(ar, nn))