#!/usr/bin/env python3

S = set(input())

if len(S) % 2 != 0:
    print("No")
elif ("N" in S and not "S" in S) or ("S" in S and not "N" in S) or ("W" in S and not "E" in S) or ("E" in S and not "W" in S):
    print("No")
else:
    print("Yes")





