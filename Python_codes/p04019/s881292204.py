def solve():
    S = input()
    n = S.count('N')
    e = S.count('E')
    w = S.count('W')
    s = S.count('S')
    if (n and not s) or (not n and s) or (e and not w) or (not e and w):
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    solve()