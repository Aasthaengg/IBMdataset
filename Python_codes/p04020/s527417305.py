N = int(input())
Ls,L = [],[]
for i in range(N):
    A = int(input())
    if A==0:
        Ls.append(L)
        L = []
    else:
        L.append(A)
Ls.append(L)
out = 0
for L in Ls:
    out += sum(L)//2
print(out)
