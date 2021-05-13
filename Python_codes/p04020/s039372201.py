n = int(input())
alst = [int(input()) for _ in range(n)]
cnt = 0
bef = 0
for num in alst:
    cnt += (num + bef) // 2
    if (num + bef) % 2 == 1 and num > 0:
        bef = 1
    else:
        bef = 0
print(cnt)