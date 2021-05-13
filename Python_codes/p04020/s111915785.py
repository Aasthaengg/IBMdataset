n = int(input())
a = []
from collections import Counter
for _ in range(n):
    a.append(int(input()))
a = [0] + a
    
cursum = 0
ans = 0
for i in range(1,n+1):
    if a[i] == 0:
        ans += cursum // 2
        cursum = 0
    else:
        cursum += a[i]
        
ans += cursum // 2
print(ans)