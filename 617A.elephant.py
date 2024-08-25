def elephant(n):
    if n < 5:
        return 1
    count = 0
    while n > 5:
        n -= 5
        count += 1
    if n > 0:
        count += 1
    return count


x = int(input())
print(elephant(x))