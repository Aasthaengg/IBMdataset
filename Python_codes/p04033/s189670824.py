a,b = map(int,input().split())
if a < 0 and b > 0:
    print("Zero")
elif a == 0 or b == 0:
    print("Zero")
elif a > 0:
    print("Positive")
else:
    n_c = b-a+1
    if n_c % 2 == 0:
        print("Positive")
    else:
        print("Negative")