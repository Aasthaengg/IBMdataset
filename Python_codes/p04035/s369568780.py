n, l = map(int, input().split())
a = list(map(int, input().split()))

pos = -1

for i in range(n-1):
    if a[i] + a[i+1] >= l:
        pos = i
        break
if pos == -1:
    print('Impossible')
    exit()

print('Possible')
for i in range(pos):
    print(i+1)

for i in reversed(range(pos+1,n-1)):
    print(i+1)

print(pos+1)

