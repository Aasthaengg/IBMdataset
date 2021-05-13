N, L = [int(x) for x in input().split()]                                   
S = [input() for _ in range(N)]

def f(s, p=0):
    for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if s[p] == c:
            if p == L - 1:
                return (i, )
            else:
                return (i, ) + f(s, p + 1)

print("".join([x[1] for x in sorted([(f(s), s) for s in S])]))