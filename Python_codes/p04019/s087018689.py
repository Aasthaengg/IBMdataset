s = input()
S = s.count("S")
E = s.count("E")
N = s.count("N")
W = s.count("W")
if (N==0 and S != 0) or (S==0 and N != 0):
    print("No")
elif (E==0 and W != 0) or (W==0 and E != 0):
    print("No")
else:
    print("Yes")