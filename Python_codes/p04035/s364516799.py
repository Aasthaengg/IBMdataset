# 解説見た

from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def solve(N, L, a):
    for knot, pair in enumerate(pairwise(a), 1):
        if sum(pair) >= L:
            break
    else:
        return []
        # 隣接和は全てL未満のため、最後の一つを外せない

    ans = []
    for i in range(1, knot):
        ans.append(i)
    for i in range(N - 1, knot - 1, - 1):
        ans.append(i)
    return ans


if __name__ == '__main__':
    N, L = map(int, input().split())
    a = tuple(map(int, input().split()))
    ans = solve(N, L, a)
    if ans:
        print('Possible')
        print(*ans, sep='\n')
    else:
        print('Impossible')
