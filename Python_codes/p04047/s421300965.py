N =int(input())
Ls = sorted(map(int,input().split()))
ans = [min(Ls[i+1],Ls[i]) for i in range(0,len(Ls)-1,2)]
print(sum(ans))