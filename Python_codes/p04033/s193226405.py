#!/usr/bin/env python3

a,b = [int(x) for x in input().split(" ")]

if a <= 0 and b >= 0:
    print("Zero")
elif a > 0:
    print("Positive")
elif (b - a) % 2 == 0:
    print("Negative")
else:
    print("Positive")
    
