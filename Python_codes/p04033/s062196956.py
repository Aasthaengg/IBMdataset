a, b = map(int, input().split())
if b > 0 and a < 0:
    ans = 2
elif b <= 0:
    if b == 0:
        ans = 2
    else:
        ans = (a - b) % 2
else:
    if b == 0:
        ans = 2
    else:
        ans = 1
if ans == 0:
    print("Negative")
elif ans == 1:
    print("Positive")
else:
    print("Zero")