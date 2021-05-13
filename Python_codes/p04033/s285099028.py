#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    a,b = map(int,input().split())
    if a == 0 or b ==0 or (a<0 and b>0):
        print("Zero")
        exit()
    else:
        if a > 0 and b > 0:
            print("Positive")
        elif abs(a-b)%2!=0:
            print("Positive")
        else:
            print("Negative")

if __name__=="__main__":
    main()