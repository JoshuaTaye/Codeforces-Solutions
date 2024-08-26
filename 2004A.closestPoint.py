def closestPoint(points):
    results = []
    for i in range(len(points)):
        if len(points[i]) > 2:
            results.append("NO")
        else:
            if abs(points[i][0] - points[i][1]) > 1:
                results.append("YES")
            else:
                results.append("NO")
    for k in results:
        print(k)

n = int(input())
arr = []
for j in range(n):
    nn = int(input())
    x = list(map(int, input().split()))
    arr.append(x)
closestPoint(arr)



