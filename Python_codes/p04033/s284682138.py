a,b = map(int,input().split())

if a > 0:
    ans = 1
elif a <= 0 and b >= 0:
    ans = 0
else:
    if (b-a+1)%2 == 0:
        ans = 1
    else:
        ans = -1
if ans == 1:
    print("Positive")
elif ans == 0:
    print("Zero")
else:
    print("Negative")