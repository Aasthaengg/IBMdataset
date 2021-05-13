N = int(input())
A = list(map(int,input().split()))
X,out = round(sum(A)/N),0
for i in range(N):
    out += (A[i]-X)**2
print(out)
