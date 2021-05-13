import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    n = S.count("N")
    s = S.count("S")
    w = S.count("W")
    e = S.count("E")

    if (n == 0 and s != 0) or (n != 0 and s == 0) or (w != 0 and e == 0) or (w == 0 and e != 0):
        print("No")
    else:
        print("Yes")


    
    
    
    

if __name__ == '__main__':
    main()

