n, L = map(int, input().split())
a = list(map(int, input().split()))
st = -1
for i in range(n-1):
    if a[i] + a[i+1] >= L:
        st = i
        break
if st < 0:
    print("Impossible")
else:
    print("Possible")
    for i in range(st):
        print(i+1)
    for i in range(n-2, st, -1):
        print(i+1)
    print(st+1)