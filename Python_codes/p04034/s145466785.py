n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(m)]

ball_cnt = [1] * 10**6
check = [0] * 10**6

check[1] += 1

for i in range(m):
    x = li[i][0]
    y = li[i][1]
    
    if check[x] == 1:
        check[y] = 1
    
    ball_cnt[x] -= 1
    ball_cnt[y] += 1
    
    if ball_cnt[x] == 0:
        check[x] = 0
        
print(sum(check))