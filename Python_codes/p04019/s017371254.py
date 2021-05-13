S=input()
if S.count("N")>=1 and S.count("S")==0:
    print("No")
elif S.count("S")>=1 and S.count("N")==0:
    print("No")
elif S.count("W")>=1 and S.count("E")==0:
    print("No")
elif S.count("E")>=1 and S.count("W")==0:
    print("No")
else:
    print("Yes")