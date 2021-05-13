s = input()
s,n,e,w = s.count("S"),s.count("N"),s.count("E"),s.count("W")
if (s > 0 and n == 0) or (s == 0 and n > 0):
    print("No")
elif (e > 0 and w == 0) or (e == 0 and w > 0):
    print("No")
else:
    print("Yes")