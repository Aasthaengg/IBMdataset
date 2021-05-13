a,b = map(int, input().split())
if a > 0 and b > 0:
    print("Positive")
elif a < 0 and b > 0:
    print("Zero")
elif a == 0 or b == 0:
    print("Zero")
else:
    d = abs(a) - abs(b)
    if d % 2 == 1:
        print("Positive")
    else:
        print("Negative")
