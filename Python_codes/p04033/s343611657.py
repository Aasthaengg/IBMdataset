a, b = map(int, input().split())
if b < 0:
    if (b - a) % 2 == 0:
        print("Negative")
    else:
        print("Positive")
elif a <= 0:
    print("Zero")
else:
    print("Positive")
