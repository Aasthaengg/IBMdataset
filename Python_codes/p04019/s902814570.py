s = input()
N = s.count("N")
W = s.count("W")
S = s.count("S")
E = s.count("E")
flag = -1
if (S > 0 and N > 0) or (S == 0 and N == 0) :
    if (E > 0 and W > 0) or (E == 0 and W == 0) :
        flag = 1
if flag == 1 :
    print("Yes")
else :
    print("No")
