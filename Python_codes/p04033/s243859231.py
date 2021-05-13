from sys import stdin
a, b= [int(_) for _ in stdin.readline().rstrip().split()]
if a > 0:
    print("Positive")
elif a <= 0 and b >= 0:
    print("Zero")
elif (b - a) % 2:
    print("Positive")
else:
    print("Negative")