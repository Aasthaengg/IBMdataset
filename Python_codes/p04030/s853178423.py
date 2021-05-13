s = input().strip()
x = ""
cur = 0
for i in range(len(s)):
    if s[i]=="0":
        x += "0"
        cur += 1
    elif s[i]=="1":
        x += "1"
        cur += 1
    else:
        if cur>0:
            x = x[:-1]
            cur -= 1
print(x)