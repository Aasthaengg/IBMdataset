A,B,C = map(int,input().split())
if A == 5:
    if B == 5:
        if C == 7:
            print("YES")
        else:
            print("NO")
    elif B == 7:
        if C == 5:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
elif A == 7:
    if B == 5 and C == 5:
        print("YES")
    else:
        print("NO")