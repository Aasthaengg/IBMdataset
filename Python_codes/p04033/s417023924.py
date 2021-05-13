a,b = [int(x) for x in input().split()]

if a > 0:
    print("Positive")
elif a <= 0 and b >= 0:
    print("Zero")
else:
    n = min(0,b) - a
    if n % 2 == 0:
        print("Negative")
    else:
        print("Positive")