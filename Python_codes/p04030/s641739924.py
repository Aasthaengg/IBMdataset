s = input().strip()
x = ""
for i in range(len(s)):
    if s[i]!="B":
        x = x+s[i]
    else:
        if len(x)>0:
            x = x[:-1]
print(x)