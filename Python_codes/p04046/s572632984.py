MOD=10**9+7
fact=[1]
temp=1
for i in range(1,3*10**5+1):
    temp*=i
    temp%=MOD
    fact+=[temp]

def bino(a,b):
    if a<b:
        return 0
    up=fact[a]
    down=fact[a-b]*fact[b]
    return (up*pow(down,MOD-2,MOD))%MOD

def find(H,W,A,B):
    temp=0
    for x in range(1,H-A+1):
        temp+=bino(x+B-2,x-1)*bino(W-B-1+H-x,H-x)
        temp%=MOD
    return temp

H,W,A,B=list(map(int,input().strip().split(" ")))
print(find(H,W,A,B))

