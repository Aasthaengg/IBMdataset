s=list(input())
ans=[]
for i in s:
    if i=="0":
        ans.append("0")
    if i=="1":
        ans.append("1")
    if i=="B" and len(ans)>0:
        ans.pop(-1)
print("".join(ans))