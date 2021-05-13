import sys
from collections import Counter
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, M = map(int, readline().split())
    R = [0]*(N)
    W = [1]*(N)
    R[0] = 1
    W[0] = 0
    for _ in range(M):
        x, y = map(int, readline().split())
        if R[x-1]==1 and W[x-1]>=1:
            W[x-1] -= 1
            if R[y-1]==0:
                R[y-1]+=1
            else:
                W[y-1]+=1
        elif R[x-1]==0 and W[x-1]>=1:
            W[x-1] -= 1
            W[y-1] += 1
        else:
            R[x-1] -= 1
            R[y-1] += 1
    ans = 0
    for i in range(N):
        if R[i]>=1:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()
