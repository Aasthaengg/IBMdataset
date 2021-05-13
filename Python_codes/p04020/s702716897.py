n = int(input())
ans = 0
prev = 0
for _ in range(n):
    a = int(input())
    tmp_ans = (a + prev) // 2
    ans += tmp_ans
    if tmp_ans == 0:
        prev = a % 2
    else:
        prev = (a + prev) % 2
print(ans)

