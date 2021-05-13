s=input()
S=len(s)
ans=[]

for i in range(S):
    if s[i]=="0":
        ans+="0"
    elif s[i]=="1":
        ans+="1"
    elif s[i]=="B":
        if len(ans)>=1:
            ans.pop()


print("".join(ans))