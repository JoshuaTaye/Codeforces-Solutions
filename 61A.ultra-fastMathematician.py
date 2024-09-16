def ultraMatematician(num1, num2):
    res = ''
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            res += "1"
        else:
            res += "0"
    return res


n1 = input()
n2 = input()
print(ultraMatematician(n1, n2))
