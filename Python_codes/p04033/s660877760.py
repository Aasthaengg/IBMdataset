# coding: utf-8
# Your code here!
a, b = map(int,input().split())

if a <= 0 and b >= 0:
    ans = "Zero"
elif a < 0 and b < 0:
    if (b-a)%2 == 0:
        ans = "Negative"
    else:
        ans = "Positive"
else:
    ans = "Positive"

print(ans)