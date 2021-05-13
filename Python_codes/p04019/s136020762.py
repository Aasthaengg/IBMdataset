from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007

def solve():
    str = (input().rstrip())
    W = 0
    N = 0
    S = 0
    E = 0

    for s in str:
        if(s == 'W'):
            W += 1
        elif(s =='E'):
            E += 1
        elif(s == 'N'):
            N += 1
        else:
            S += 1
    

    if(S*N*E*W > 0 or (S + N == 0 and E*W > 0) or(E +W == 0 and S*N > 0)):
        print("Yes")
    else:
        print("No")
    
if __name__ == '__main__':
    solve()
