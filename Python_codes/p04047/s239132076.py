import sys

if __name__ == "__main__":
    N = sys.stdin.readline()
    L_list = list(map(int, sys.stdin.readline().split()))
    L_list.sort()
    total_bbq = sum(L_list[::2])
    print(total_bbq)
