#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    ret = 0
    pv = 0
    for _ in range(N):
        nw = int(input())
        pa = min(pv, nw)
        ret += pa
        pv = nw - pa
        ret += pv//2
        pv = pv%2
    print(ret)

if __name__ == '__main__':
    main()