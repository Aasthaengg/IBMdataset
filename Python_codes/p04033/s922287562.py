a, b = map(int, input().split())
zero = (a == 0 | b == 0) | (a < 0 and 0 < b) | (b < 0 and 0 < a)
negative_a = (a < 0 and 0 < b) and (a + b + 1) % 2 != 0
negative_b = (a < 0 | b < 0) and (a + b + 1) % 2 != 0
if zero:
    print("Zero")
elif negative_a | negative_b:
    print("Negative")
else:
    print("Positive")