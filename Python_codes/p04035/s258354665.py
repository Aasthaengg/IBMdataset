#! /usr/bin/env python3

def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    la = N
    for i in range(N-1):
        if A[i] + A[i+1] >= L:
            la = i
            break
    if la == N:
        print('Impossible')
        return
    print('Possible')
    for i in range(la) : print(i+1)
    for i in range(N-la-2) : print(N-i-1)
    print(la+1)
if __name__ == '__main__':
    main()