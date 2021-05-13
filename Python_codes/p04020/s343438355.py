N = int(input())
ans = 0
B = 0
for i in range(N):
    A = int(input())
    C = A+B
    ans += C//2
    if B == 1 and C == 1:
        B = 0
        continue
    B = C % 2
print(ans)
