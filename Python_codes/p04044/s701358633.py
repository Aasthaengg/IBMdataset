n, l = map(int, input().split(" "))
s = []
for i in range(0, n):
    s.append(str(input()))
s.sort()
print(''.join(s))