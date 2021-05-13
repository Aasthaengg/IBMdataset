N=int(input())
ans=0
tmp=0
for i in range(N):
   s=int(input())
   if s!=0:
      tmp+=s
   else:
      ans+=tmp//2
      tmp=0
ans+=tmp//2
print(ans)