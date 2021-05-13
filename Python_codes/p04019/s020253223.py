s=set(input())
if len(s)==4:
    print("Yes")
elif len(s)%2:
    print("No")
else:
    if ("N" in s and "S" in s) or ("W"in s and "E" in s):
        print("Yes")
    else:
        print("No")
