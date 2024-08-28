def searchEasy(arr):
    for i in arr:
        if i == 1:
            return "HARD"
    return "EASY"

n = int(input())
ar = list(map(int, input().split()))
print(searchEasy(ar))