A = list(map(int, input().split()))
A.sort()
a = A[0]
b = A[1]
c = b-a

if a <= 0 <= b:
    print("Zero")

elif a > 0:
    print("Positive")

elif b < 0:
    if c%2 == 1:
        print("Positive")
    else:
        print("Negative")
