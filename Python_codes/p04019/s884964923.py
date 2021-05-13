#!/usr/bin/env python3

def main():
    S = input()

    s = len([1 for _ in S if _ == 'S'])
    n = len([1 for _ in S if _ == 'N'])
    e = len([1 for _ in S if _ == 'E'])
    w = len([1 for _ in S if _ == 'W'])

    if (s > 0 and n > 0) or (s == n == 0):
        flag1 = True
    else:
        flag1 = False
    if (e > 0 and w > 0) or (e == w == 0):
        flag2 = True
    else:
        flag2 = False
    
    if flag1 and flag2:
        print('Yes')
    else:
        print('No')

main()