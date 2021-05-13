n, l = map(int, input().split())
a = list(map(int, input().split()))

atom = -1
for i in range(n-1):
    if l <= a[i] + a[i+1]:
        atom = i
        break
        
if atom < 0:
    print('Impossible')
else:
    print('Possible')
    for i in range(atom):
        print(i+1)
    for i in range(n-atom-1):
        print(n-1-i)