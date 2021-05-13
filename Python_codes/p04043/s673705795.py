import math

n = list(map(int,input().split()))
a = sum(n[i] == 5 for i in range(3))
b = sum(n[i] == 7 for i in range(3))
if a == 2 and b == 1:
    print("YES")
else:
    print("NO")