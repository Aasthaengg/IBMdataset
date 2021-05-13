a, b = map(int, input().split())
if 0 < a:
    print("Positive")
    exit()
elif a == 0 or b == 0 or (a < 0 and 0 < b):
    print("Zero")
    exit()
else:
    diff = abs(a-b)+1
    if diff%2 == 0:
        print("Positive")
    else:
        print("Negative")
