a,b = map(int,input().split())

if a == 0 or b == 0 or (a < 0 and 0 < b) or (0 < a and b < 0):
    print ("Zero")
else:
    x = b - a
    if 0 < a and 0 < b:
        print ("Positive")
    else:
        if x%2 == 0:
            print ("Negative")
        else:
            print ("Positive")
