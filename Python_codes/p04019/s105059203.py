s = set(list(input()))

if any(s == set(list(i)) for i in ["NS","EW","NEWS"]):
    print("Yes")
else:
    print("No")