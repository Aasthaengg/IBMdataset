# -*- coding: utf-8 -*-

if __name__ == "__main__":
    N, L = map(int, input().split())
    si = []
    for i in range(N):
        si.append(str(input()))
    si.sort()
    print(''.join(si))
