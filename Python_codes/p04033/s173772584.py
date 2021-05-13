a,b = map(int,input().split())
ans = "Positive"

if b < 0:
    if (b-a+1) % 2 != 0:
        ans = "Negative"
    
if a * b <= 0:
    ans = "Zero"
    
print(ans)