a, b = map(int, input().split())

# p = max(1, b) - max(1, a) + 1
n = min(-1, b) - min(0, a) + 1

if a <= 0 <= b:
    print("Zero")
elif n % 2 == 0:
    print("Positive")
else:
    print("Negative")
