n, l = map(int,input().split())
A = list(map(int,input().split()))

last = -1
for i in range(n-1):
    if A[i] + A[i+1] >= l:
        last = i
        break

if last == -1:
    print("Impossible")
else:
    print("Possible")
    for i in range(last):
        print(i+1)
    for i in range(n-2, last-1, -1):
        print(i+1)
