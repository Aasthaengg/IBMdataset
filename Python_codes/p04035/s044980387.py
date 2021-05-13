N,L = map(int, input().split())
A = [int(a) for a in input().split()]

l = 0
r = N-1
s = sum(A)
ans = []
while l < r:
    if s < L:
        break
    if r-l > 1:
        if A[l]+A[l+1] < L:
            s -= A[l]
            ans.append(l+1)
            l += 1
            continue
        if A[r]+A[r-1] < L:
            s -= A[r]
            ans.append(r)
            r -= 1
            continue
    if A[l] < A[r]:
        ans.append(l+1)
        s -= A[l]
        l += 1
    else:
        ans.append(r)
        s -= A[r]
        r -= 1
        
if len(ans) == N-1:
    print("Possible")
    for a in ans:
        print(a)
else:
    print("Impossible")