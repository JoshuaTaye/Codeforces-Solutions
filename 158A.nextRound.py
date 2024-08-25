def nextRound(n, k):
    score = int(n[k-1])
    participants = 0
    for i in n:
        if int(i) >= score and int(i) > 0:
            participants += 1
        else:
            return participants
    return participants
init = input()
init = init.split(" ")
sec = input()
sec = sec.split(" ")
print(nextRound(sec, int(init[1])))
