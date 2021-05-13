import sys
input = sys.stdin.readline
from collections import Counter
def main():
    S = input().rstrip()
    C = Counter(S)
    n = C['N']
    s = C['S']
    w = C['W']
    e = C['E']
    if (n != 0 and s != 0) or (n == 0 and s == 0):
        if (w != 0 and e != 0) or (w == 0 and e == 0):
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()