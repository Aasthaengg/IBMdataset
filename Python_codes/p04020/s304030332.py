n = int(input())
a = [int(input()) for i in range(n)]
ans = 0
for i in range(n-1):
  if a[i]%2==0:
    ans+=a[i]//2
  elif a[i+1]>0:
    ans+=1
    a[i]-=1
    ans+=a[i]//2
    a[i+1]-=1
  else:
    ans+=a[i]//2    
  #print(ans)
  
ans+=a[n-1]//2
print(ans)