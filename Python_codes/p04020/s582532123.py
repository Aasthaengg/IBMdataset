N = int(input())

ans = 0
n = 0
for i in range(N):
    a = int(input())
    if(a != 0 and n > 0):
        ans += 1
        a -= 1
        n = 0
    elif(a == 0):
        n = 0
        
    if(a > 1):
        ans += a//2
        n = a%2
    
print(ans)