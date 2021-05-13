def resolve():
    S = str(input())
    n = S.count('N')
    s = S.count('S')
    w = S.count('W')
    e = S.count('E')
    if n > 0 and s == 0:
        print('No')
        return
    if n == 0 and s > 0:
        print('No')
        return
    if w > 0 and e == 0:
        print('No')
        return
    if w == 0 and e > 0:
        print('No')
        return
    print('Yes')

    return


resolve()