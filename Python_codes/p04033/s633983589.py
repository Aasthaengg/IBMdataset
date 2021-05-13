a, b = map(int, input().split())
if a<= 0 <=b:
    print("Zero")

elif a > 0:
    print("Positive")

else:
    b = min(b,1)
    a *= -1
    print("Positive" if (a-b)%2 == 1 else "Negative")
