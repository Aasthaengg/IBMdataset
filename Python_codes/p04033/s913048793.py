import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a,b=MI()
    
    if a<=0<=b:
        print("Zero")
    
    elif a>0 and b>0:
        print("Positive")
    else:
        if b>0:
            b=-1
        n=(b-a+1)
        if n%2==0:
            print("Positive")
        else:
            print("Negative")

main()
