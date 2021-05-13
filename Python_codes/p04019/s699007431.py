s = input()
flag = [0] * 4
for i in range(len(s)):
    if s[i] == "N":
        flag[0] = 1
    elif s[i] == "W":
        flag[1] = 1
    elif s[i] == "S":
        flag[2] = 1
    else:
        flag[3] = 1

print("Yes" if flag[0] == flag[2] and flag[1] == flag[3] else "No")