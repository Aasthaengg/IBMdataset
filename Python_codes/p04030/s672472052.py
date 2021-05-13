s=input()
ans=[]
for i in s:
    if i!="B":
        ans.append(i)
    else:
        ans=ans[:-1]
        
print("".join(ans))