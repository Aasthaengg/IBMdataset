N = int(input())
ans = 0
b = 0
for i in range(N):
    a = int(input())
    ans += (a + b) // 2
    if (a + b) % 2 == 1:
        if a > 0:
            b = 1
        else:
            b = 0
    else:
        b = 0
        
print(ans)