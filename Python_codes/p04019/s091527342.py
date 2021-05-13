import sys


def resolve(in_):
    S = next(in_).strip()
    
    H = None
    W = None

    for c in S:
        if c == 'N':
            if H == 'S':
                H = False
            elif H is None:
                H = c
        elif c == 'S':
            if H == 'N':
                H = False
            elif H is None:
                H = c
        elif c == 'W':
            if W == 'E':
                W = False
            elif W is None:
                W = c
        elif c == 'E':
            if W == 'W':
                W = False
            elif W is None:
                W = c
    
    return not (H or W)
    
    return True


def main():
    answer = resolve(sys.stdin)
    print('Yes' if answer else 'No')


if __name__ == '__main__':
    main()
