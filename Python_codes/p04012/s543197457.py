import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()

def main():
    w = input()
    d = defaultdict(int)
    for c in w: d[c] += 1
    cond = True
    for key in d:
        if d[key] % 2 != 0:
            cond = False
            break
    if cond:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
