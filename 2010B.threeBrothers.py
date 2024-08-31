def threeBrothers(nums):
    for i in range(1, 4):
        if i not in nums:
            return i

ar = list(map(int, input().split()))
print(threeBrothers(ar))