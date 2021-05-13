s=input()
res=""
for i in range(len(s)):
    if s[i]!="B":
        res+=s[i]
    else:
        res=res[:-1]
print(res)