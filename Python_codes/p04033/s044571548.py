import sys
import bisect
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline

def main():
    a,b = map(int,read().split())
    if a > 0:
        print("Positive")
    elif b < 0:
        if (b - a)%2 == 1:
            print("Positive")
        else:
            print("Negative")
    else:
        print("Zero")
    
if __name__ == '__main__':
    main()
