x, y = map(int, input().split())
if 0 < x <= y:
    print("Positive")
elif x <= y < 0:
    if (y-x+1) % 2 == 0:
        print("Positive") 
    else:
        print("Negative")
else:
    print("Zero")
