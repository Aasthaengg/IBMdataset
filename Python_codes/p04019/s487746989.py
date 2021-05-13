s = list(input())
ss = set(s)
if (("W" in ss and "E" not in ss) or ("S" in ss and "N" not in ss) 
    or ("E" in ss and "W" not in ss) or ("N" in ss and "S" not in ss)):
    print("No")
else:
    print("Yes")