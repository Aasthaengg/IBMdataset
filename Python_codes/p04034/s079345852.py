n, m = map(int,input().split())
b_list = []

for i in range(m):
    x = []
    x = list(map(int,input().split()))
    b_list.append(x)

ans_list = [0 for i in range(10**5)]
ans_list[0] = 1
ball_list = [1 for i in range(10**5)]

for tmp in b_list:
    x, y = tmp[0], tmp[1]
    if ans_list[x-1] == 1 and ans_list[y-1] == 0:
        ans_list[y-1] += 1
    ball_list[y-1] += 1
    ball_list[x-1] -= 1
    if ball_list[x-1] == 0:
        ans_list[x-1] = 0

ans = 0

for i in ans_list:
    if i == 1:
        ans += 1

print(ans)
