n, l = map(int, input().split())
a = list(map(int, input().split()))

check_min = 0
index_min = n

for i in range(n-1):
    if check_min < a[i] + a[i+1]:
        check_min = a[i] + a[i+1]
        index_min = i

if check_min < l:
    print('Impossible')
else:
    print('Possible')
    for i in range(index_min):
        print(i+1)
    for i in range(n-2, index_min, -1):
        print(i+1)
    print(index_min+1)
