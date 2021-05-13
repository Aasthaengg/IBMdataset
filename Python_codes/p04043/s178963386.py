from sys import stdin

A,B,C = [int(x) for x in stdin.readline().rstrip().split()]

if A + B + C == 17 and A >= 5 and B >= 5 and C >= 5:
        print("YES")
else:
        print("NO")
