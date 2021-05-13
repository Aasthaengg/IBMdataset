n = int(input())
ai = [int(input()) for i in range(n)]

ans = 0
nokori = 0

for i in range(n):
    if ai[i] % 2 == 1:
        if nokori == 1:
            nokori = 0
            ans += ai[i] // 2 + 1
        else:
            nokori = 1
            ans += ai[i] // 2
    elif ai[i] > 0:
        if nokori == 1:
            ans += ai[i] // 2
            nokori = 1
        else:
            ans += ai[i] // 2
            nokori = 0
    elif ai[i] == 0:
        nokori = 0

print(ans)