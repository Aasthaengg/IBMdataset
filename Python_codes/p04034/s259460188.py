import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    N,M=map(int,input().split())
    X, Y = [0] * M, [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())

    red=[True]+[False]*(N-1)
    cnt=[1]*N

    for i in range(M):
        cnt[X[i]-1]-=1
        cnt[Y[i]-1]+=1
        if red[X[i]-1]:
            red[Y[i]-1]=True
        if cnt[X[i]-1]==0:
            red[X[i] - 1]=False

    print(red.count(True))


resolve()