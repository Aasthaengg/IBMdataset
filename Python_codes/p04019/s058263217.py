S=input()
n="N" in S
w="W" in S
e="E" in S
s="S" in S
if (n == s) and (e == w):
    print("Yes")
else:
    print("No")
