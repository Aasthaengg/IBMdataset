a, b = map(int, input().split())

# == 0
if ((a == 0) or (b == 0) or (a < 0 and b > 0)):
    print("Zero")
    exit(0)

# > 0
if (a > 0 and b > 0):
    print("Positive")
    exit(0)

if (b - a + 1) % 2 == 0:
    print("Positive")
    exit(0)

# < 0
print("Negative")
