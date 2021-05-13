import sys

input = sys.stdin.readline

def main():
    snflg = True
    ewflg = True
    S = input().rstrip('\n')
    if 'S' in S or 'N' in S:
        snflg = False       
        if 'S' in S and 'N' in S:
            snflg = 'Yes'
    if 'E' in S or 'W' in S:
        ewflg = False
        if 'E' in S and 'W' in S:
            ewflg = 'Yes'
    if snflg and ewflg:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()