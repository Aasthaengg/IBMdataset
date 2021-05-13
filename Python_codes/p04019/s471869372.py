N = str(input())

if N.count("N") > 0 and N.count("W") > 0 and N.count("S") > 0 and N.count("E") > 0:
    print("Yes")
elif N.count("N") > 0 and N.count("W") == 0 and N.count("S") > 0 and N.count("E") == 0:
    print("Yes")
elif N.count("N") == 0 and N.count("W") > 0 and N.count("S") == 0 and N.count("E") > 0:
    print("Yes")
else:
    print("No")
