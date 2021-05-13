def resolve():
    a, b = [int(i) for i in input().split()]
    if a <= 0 and 0 <= b:
        print("Zero")
    else:
        if a > 0:
            print("Positive")
        else:
            if (abs(b - a) + 1) % 2 == 0:
                print("Positive")
            else:
                print("Negative")


resolve()
