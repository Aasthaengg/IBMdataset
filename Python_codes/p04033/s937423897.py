a, b = map(int, input().split())
ans = 1

if a > 0 and b > 0:
    print("Positive")
elif a == 0:
    print("Zero")
elif a < 0 and b > 0:
    print("Zero")
elif b == 0:
    print("Zero")
elif a < 0 and b < 0:
    diff = b - a
    if diff % 2 == 0:
        print("Negative")
    elif diff % 2 != 0:
        print("Positive")
