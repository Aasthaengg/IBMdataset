from sys import stdin
input = stdin.readline

N, L = map(int, input().split())
D = []

for i in range(N):
    D.append(input().strip())
D.sort()
print(''.join(D))