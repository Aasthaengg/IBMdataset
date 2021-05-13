n = int(input())
s = list(map(int, input().split()))
s = sorted(s)
c, f = 0, []
for i in range(0, 2*n, 2):
    c+=min(s[i], s[i+1])
    # print(min(s[i], s[i+1]))
print(c)