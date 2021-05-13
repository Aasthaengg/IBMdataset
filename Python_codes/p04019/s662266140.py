S=input()
if (("S" not in S) and ("N" in S)) or (("S" in S) and ("N" not in S)):
    print("No")
elif (("W" not in S) and ("E" in S)) or (("W" in S) and ("E" not in S)):
    print("No")
else:
    print("Yes")