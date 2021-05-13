N=int(input())
M=sorted(list(map(int,input().split())))
if N%2==1:
    M.pop(-1)
print(sum(M[::2]))