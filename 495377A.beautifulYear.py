def beautifulYear(n):
    for i in range(n+1, 9001):
        arr = []
        for j in str(i):
            if j not in arr:
                arr.append(j)
        if len(arr) >= 4:
            return i

x = int(input())
print(beautifulYear(x))
