S=str(input())
ans=""
for i in range(len(S)):
    if S[i]=="B":
        ans=ans[:len(ans)-1]
    else:
        ans+=S[i]
print(ans)