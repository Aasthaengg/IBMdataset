N,L = map(int,input().split())
*A, = map(int,input().split())

S = [0]*(N+1)
for i,a in enumerate(A): S[i+1] = S[i] + a
ans = []
i=0
j=N-1
while i<j:
    if S[j+1]-S[i] < L:
        print("Impossible")
        break
    if A[i]+A[i+1] <= A[j]+A[j-1]:
        ans.append(i+1)
        i+=1
    else:
        ans.append(j)
        j-=1
else:
    print("Possible")
    for a in ans: print(a)