import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    L=[0]*N
    L[0]=1
    cnt=[1]*N
    for i in range(M):
        x,y=MI()
        x-=1
        y-=1
        if L[x]==1:
            L[y]=1
            if cnt[x]==1:
                L[x]=0
                flag=0
        cnt[x]-=1
        cnt[y]+=1
                
    print(sum(L))
        

main()
