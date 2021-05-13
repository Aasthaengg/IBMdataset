N = int(input())
L = sorted(list(map(int,input().split())))
print(sum(i for i in L[::2]))