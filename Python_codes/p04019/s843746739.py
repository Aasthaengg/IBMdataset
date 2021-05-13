s=input()
N=s.count("N")
W=s.count("W")
S=s.count("S")
E=s.count("E")
if N==0 and S==0:
    if E==0 and W==0:
        print("Yes")
    elif E>0 and W>0:
        print("Yes")
    else:
        print("No")
elif N>0 and S>0:
    if E==0 and W==0:
        print("Yes")
    elif E>0 and W>0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
