S = list(input())

n = S.count("N")
s = S.count("S")
e = S.count("E")
w = S.count("W")

if n!=0 and s!=0 and e==0 and w==0:
    print("Yes")
elif n==0 and s==0 and e!=0 and w!=0:
    print("Yes")
elif n!=0 and s!=0 and e!=0 and w!=0:
    print("Yes")
else:
    print("No")