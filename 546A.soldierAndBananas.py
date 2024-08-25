def soldierAndBananas(w):
    k = int(w[0])
    multiplier = 1
    init = int(w[1])
    num = int(w[2])
    total = 0
    for i in range(num):
        total += k * multiplier
        multiplier += 1
    if total > init:
        return total - init
    return 0


n = input()
n = n.split(" ")
print(soldierAndBananas(n))