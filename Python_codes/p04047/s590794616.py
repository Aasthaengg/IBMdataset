n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)
ans=0
c=0
for i in range(0,len(a),2):
    if c>n:
        break
    #print(a[i],a[i+1],min(a[i],a[i+1]))
    ans+=min(a[i],a[i+1])
    c+=1
print(ans)
