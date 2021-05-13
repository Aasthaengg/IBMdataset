#

import sys
from copy import deepcopy
input=sys.stdin.readline

def main():
    a,b=map(int,input().split())
    if a*b<=0:
        print("Zero")
    elif a>0:
        print("Positive")
    else:
        pm=(b-a+1)
        if pm%2==0:
            print("Positive")
        else:
            print("Negative")
    
if __name__=="__main__":
    main()
