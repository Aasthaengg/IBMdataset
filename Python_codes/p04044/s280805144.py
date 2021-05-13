n, l = map(int, input().split())
a = []
for _ in range(n):
    a.append(input())
a.sort()
print(''.join(a))