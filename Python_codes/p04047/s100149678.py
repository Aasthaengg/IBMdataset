A = int(input())
B = list(map(int,input().split()))
B.sort(reverse=True)
ans =0
for i in range(A):
    ans += min(B[0+i*2],B[1+i*2])
print(ans)