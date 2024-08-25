def boyOrGirl(user):
    st = []
    for i in user:
        if i not in st:
            st.append(i)
    if len(st)% 2 == 0:
        return "CHAT WITH HER!"
    return "IGNORE HIM!"

n = input()
print(boyOrGirl(n))