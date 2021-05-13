import sys

input = sys.stdin.readline

def main():
    S = input().rstrip('\n')
    if (('S' in S) == ('N' in S)) and (('E' in S) == ('W' in S)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()