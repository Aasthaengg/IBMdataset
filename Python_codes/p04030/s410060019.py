s=input()

ans=""
for i in range(len(s)):
    if s[i]=="B":
        if len(ans)==0:
            continue
        ans=ans[:-1]
    else:
        ans+=s[i]
print(ans)
