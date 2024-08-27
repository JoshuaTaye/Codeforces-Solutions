def vanyaAndFence(arr, n):
    width = len(arr)
    for i in range(len(arr)):
        if arr[i] > n:
            width += 1
    return width


n = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(vanyaAndFence(arr, n[1]))