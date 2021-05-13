S = input()
e = S.count("E")
w = S.count("W")
n = S.count("N")
s = S.count("S")

ew_flag = False
ns_flag = False

if (e > 0 and w > 0) or (e == 0 and w == 0):
  ew_flag = True
if (n > 0 and s > 0) or (n == 0 and s == 0):
  ns_flag = True

if ew_flag and ns_flag:
  print("Yes")
else:
  print("No")