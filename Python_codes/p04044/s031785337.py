N,L=map(int,input().split())
s = [input() for _ in range(N)]
s = sorted(s)
print(''.join(s))