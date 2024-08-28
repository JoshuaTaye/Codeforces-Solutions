def queueAtTheSchool(qu, n):
    q = list(qu)
    while n > 0:
        i =  0
        while i < (len(q) - 1):
            if q[i] == "B" and q[i+1] == "G":
                q[i], q[i+1] = q[i+1], q[i]
                i += 1
            i += 1
        n -= 1
    final = ''
    for i in q:
        final += i
    return final

n = list(map(int, input().split()))
queue = input()
print(queueAtTheSchool(queue, n[1]))