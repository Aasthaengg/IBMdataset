N, L = map(int,input().split())

A = list(map(int,input().split()))

MAX = 0
index = -1

for i in range(N-1):
    if A[i] + A[i+1] > MAX:
        MAX = A[i] + A[i+1]
        index = i+1

if MAX < L:
    print("Impossible")
else:
    print("Possible")
    for i in range(1,index):
        print(i)
    for i in range(N-1,index,-1):
        print(i)
    print(index)