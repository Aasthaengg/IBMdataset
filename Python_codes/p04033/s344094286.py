a, b = map(int, input().split())
if a <= 0 <= b:
    print("Zero")
elif 1 <= a or (b-(a-1))%2 == 0:
    print("Positive")
else:
    print("Negative")