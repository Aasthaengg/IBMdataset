import sys
input = sys.stdin.readline

A = input().rstrip('\n')

N = A.count("N")
S = A.count("S")
W = A.count("W")
E = A.count("E")

if (N == 0 or S == 0) and N + S != 0:
    print("No")
    exit()
if (W == 0 or E == 0) and W + E != 0:
    print("No")
    exit()
print("Yes")
