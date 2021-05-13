x=list(map(int,input().split()))
ans="NO"
if x.count(7)==1 and x.count(5)==2:
    ans="YES"
print(ans)