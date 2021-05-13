N = int(input())
Llist = sorted(list(map(int, input().split())))[::-1]
ans = 0
for i in range(0, 2*N, 2):
    ans += min(Llist[i], Llist[i+1])
print(ans)
