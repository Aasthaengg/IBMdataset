from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,l=nii()
s=[input() for i in range(n)]
s.sort()

print(''.join(s))