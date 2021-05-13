n = int(input())
ai = [int(input()) for i in range(n)]

ans = 0
nokori = 0

ans = ai[0] // 2
ai[0] %= 2

for i in range(1,n):
    if ai[i] > 0:
        ans += ai[i] // 2
        if ai[i] % 2 == 1:
            if ai[i-1] == 1:
                ans += 1
            else:
                ai[i] = 1
        else:
            if ai[i-1] == 1:
                ai[i] = 1

print(ans)