t=input()
n=t.count("N")
w=t.count("W")
s=t.count("S")
e=t.count("E")
if ((n>=1 and s>=1 and w==0 and e==0) or (w>=1 and e>=1 and n==0 and s==0) or (n>=1 and s>=1 and w>=1 and e>=1)):
    print("Yes")
else:
    print("No")