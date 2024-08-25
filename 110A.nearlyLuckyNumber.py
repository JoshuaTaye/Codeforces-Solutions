def nearlyLuckyNumber(number):
    summ = 0
    for i in number:
        if i == "4" or i == "7":
            summ += 1
    if summ == 4 or summ == 7:
        return "YES"
    return "NO"

n = input()
print(nearlyLuckyNumber(n))