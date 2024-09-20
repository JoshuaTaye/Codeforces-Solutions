def isYourHorseOnTheOtherRoof(arr):
    res = 0
    for i in range(len(arr)):
        if arr[i] in arr[:i]:
            res += 1
    return res

arr = list(map(int, input().split()))
print(isYourHorseOnTheOtherRoof(arr))