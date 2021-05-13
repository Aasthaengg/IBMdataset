n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = [j for i,j in enumerate(l) if i%2 == 0]
print(sum(ans))
