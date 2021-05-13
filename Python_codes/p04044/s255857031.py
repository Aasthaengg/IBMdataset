N,L = [int(i) for i in input().split()]
S = [input() for _ in range(N)]

S.sort()
[print(i,end='') for i in S]
