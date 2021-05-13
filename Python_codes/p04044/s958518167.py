n, l = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
s_sorted = sorted(s)
print(''.join(s_sorted))