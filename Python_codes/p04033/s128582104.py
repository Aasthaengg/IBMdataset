a, b = map(int, input().split())

if a <= 0 and 0 <= b:
    print("Zero")
elif a < 0 and b < 0:
    if (abs(a)-abs(b)+1) % 2 == 1:
        print("Negative")
    else:
        print("Positive")
else:
    print("Positive")
