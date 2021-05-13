n = int(input())

a = list(map(int,input().split()))

ans = 100010001000

for i in range(-100,101):
    total = 0
    for j in a:
        total += (j-i)**2
    
    ans = min(ans,total)
    
print(ans)