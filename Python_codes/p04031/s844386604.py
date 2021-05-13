a = int(input())
b = list(map(int,input().split()))
ans = 4000000

for i in range(-100,101):
    ans_sub = 0
    for j in range(a):
        ans_sub += (b[j]-i)**2
    ans = min(ans,ans_sub)
print(ans)