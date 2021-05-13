N,M = map(int, input().split())

ans = set([0])
cnt = [1] * N
for _ in range(M):
    x,y = [int(i) - 1 for i in input().split()]
    cnt[x] -= 1; cnt[y] += 1
 
    if x in ans:
        ans.add(y)
        if cnt[x] == 0: # 絶対に赤いボールがyに移される
            ans.remove(x)
 
print(len(ans))