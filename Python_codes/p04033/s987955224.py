a, b = map(int, input().split())

if a <= 0 <= b:
    print("Zero")
elif 0 < a <= b:
    print("Positive")
elif a < 0 and 0 < b:
    if a % 2 == 0:
        print("Positive")
    else:
        print("Negative")
else:
    if (b - a) % 2 == 0:
        print("Negative")
    else:
        print("Positive")
