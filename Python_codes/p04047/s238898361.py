def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
    
n=I()
a=LI()
a.sort()

ans=0
for i in range(n):
    ans+=min(a[2*i],a[2*i+1])

print(ans)