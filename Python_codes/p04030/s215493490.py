s=input()
ans=""
for i in range(len(s)):
    x=s[i]
    if x=="0":
        ans+="0"
    elif x=="1":
        ans+="1"
    else:
        if len(ans)!=0:
            ans=ans[:-1]
print(ans)
