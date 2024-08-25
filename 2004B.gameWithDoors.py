def gameWithDoors(arr):
    output = []
    for i in arr:
        x = max(i[0][0], i[1][0],i[0][1], i[1][1])
        count = 0
        for p in range(x):
            if (i[0][0] <= p <= i[0][1] and i[1][0] <= p <= i[1][1]) or (i[0][0]<= p+1 <=i[0][1] and i[1][0]<=p<=i[1][1]) or (i[0][0]<= p <=i[0][1] and i[1][0]<= p+1 <=i[1][1]):
                count += 1
        if count == 0:
            count += 1
        output.append(count)
    for i in output:
        print(i)
n = int(input())
doors = []
for j in range(n):
    doors.append([])
    for k in range(2):
        n = input()
        o = n.split(" ")
        for l in range(len(o)):
            o[l] = int(o[l])
        doors[j].append(o)

gameWithDoors(doors)