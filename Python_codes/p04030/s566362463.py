s=list(input())
n=len(s)
ans=[]
for i in range(n):
    if s[i]!="B" :
        
        ans.append(s[i])
    else:
        if len(ans)!=0:
            ans.pop(-1)

print("".join(ans))
        

    
