N, LEN = list(map(int, input().split()))
a = []
for i in range(N):
    s = input()
    a.append(s)
b = sorted(a)
ans = "".join(b)
print(ans)