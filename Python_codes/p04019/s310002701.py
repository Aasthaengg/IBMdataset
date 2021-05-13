s = input()

N = s.count("N")
W = s.count("W")
S = s.count("S")
E = s.count("E")


if (N == S == 0 or (N > 0 and S > 0)) and (E == W == 0 or (W > 0 and E > 0)):
    print("Yes")
else:
    print("No")