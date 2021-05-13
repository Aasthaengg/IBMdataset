from math import fabs
a, b = map(int, input().split())
if a <= 0 and 0 <= b:
    print("Zero")
else:
    if a > 0:
        print("Positive")
    else:
        if (fabs(b - a) + 1) % 2 == 0:
            print("Positive")
        else:
            print("Negative") 