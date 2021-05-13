n,l=map(int,input().split())
ans=[]
for i in range(n):
    ans.append(input())
ans=sorted(ans)

a=ans[0]
for i in range(n-1):
    a=a+ans[i+1]
print(a)


        

    
