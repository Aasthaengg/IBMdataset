n = int(input())
a = []
from collections import Counter
for _ in range(n):
    a.append(int(input()))
    
a = a + [0]
    
ans = 0
for i in range(n):
    ans += a[i] // 2
    a[i] %= 2
    if a[i] == 1 and a[i+1] >= 1:
        ans += 1
        a[i] = 0
        a[i+1] -= 1
        
print(ans)