N, L = map(int, raw_input().split())
A = map(int, raw_input().split())

k = None
for i in range(N-1):
    if A[i] + A[i+1] >= L:
        k = i
        break
    
if k is None:
    print "Impossible"
else:
    print "Possible"
    for j in range(1,k+1):
        print j
    for j in range(N-1, k, -1):
        print j