a, b = map(int, input().split())

if 0 < a:
    print("Positive")
elif a == 0 or 0 <= b:
    print("Zero")
else:
    length = abs(a + b + 1)
    if length % 2 == 0:
        print("Positive")
    else:
        print("Negative")