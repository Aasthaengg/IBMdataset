N = input()
Ls = map(int,raw_input().split(" "))

Ls.sort()
print sum(Ls[i] for i in range(0,N*2,2))