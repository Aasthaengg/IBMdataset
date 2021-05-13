a, b = [int(w) for w in input().split()]

if a * b <= 0:
    print("Zero")
elif a > 0:
    print("Positive")
else:
    if (a - b) % 2 == 0:
        print("Negative")
    else:
        print("Positive")
