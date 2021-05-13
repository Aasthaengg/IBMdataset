N = int(input())
A = list(map(int,input().split()))

def ans_one(i):
    ans=0
    for a in A:
        ans += (a-i)**2
    return ans

ans=10**20
for i in range(-102,103):
    ans_ = ans_one(i)
    if ans_ < ans:
        ans =ans_
print(ans)