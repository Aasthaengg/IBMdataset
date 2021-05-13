def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
n,l=NM()
a=[0]+L()
for i in range(1,n):
    if a[i]+a[i+1]>=l:
        print("Possible")
        for j in range(1,i):
            print(j)
        for j in range(n-1,i-1,-1):
            print(j)
        break
else:
    print("Impossible")