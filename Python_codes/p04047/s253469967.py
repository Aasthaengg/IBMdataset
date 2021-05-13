def solve(n, l):
    return sum(sorted(l)[::2])

n = int(input())
l = list(map(int, input().split()))
print(solve(n, l))