N,*L=map(int, open(0).read().split())
L=sorted(L)
print(sum(map(min, L[::2], L[1::2])))