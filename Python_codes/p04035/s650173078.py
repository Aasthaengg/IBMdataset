N, L = map(int,input().split())
a = list(map(int,input().split()))
t = True
key_number = -1
for i in range(1,N):
    if a[i] + a[i-1] >= L:
        t = False
        key_number = i

if t:
    print("Impossible")
else:
    print("Possible")
    for ans in range(1,key_number):
        print(ans)
    for ans in range(N-1,key_number-1,-1):
        print(ans)