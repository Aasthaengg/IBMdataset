a,b = map(int, input().split())
if a < 0:
    if b >= 0:
        print("Zero")
    else:
        if (a+b)%2:
            print("Positive")
        else:
            print("Negative")
elif a == 0:
    print("Zero")
else:
    print("Positive")