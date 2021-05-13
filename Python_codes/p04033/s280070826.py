#!/usr/bin/env python3
a, b = map(int, input().split())
if a > 0 and b > 0:
    print("Positive")
elif b >= 0:
    print("Zero")
else:
    if (b - a) % 2 > 0:
        print("Positive")
    else:
        print("Negative")
