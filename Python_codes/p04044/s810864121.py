n, l = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
s = sorted(s)
print(''.join(s))
