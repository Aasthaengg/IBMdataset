#!/usr/bin/env python3
from collections import Counter

def solve(S):
    s = Counter(S)
    if len(S) == 1:
        return "No"
    elif (s["N"]*s["S"] == 0 and s["N"]+s["S"] > 0) or \
         (s["E"]*s["W"] == 0 and s["E"]+s["W"] > 0):
        return "No"
    else:
        return "Yes"

def main():
    S = input()
    print(solve(S))

if __name__ == '__main__':
    main()