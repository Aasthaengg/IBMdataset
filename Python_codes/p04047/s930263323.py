N = int(raw_input())
L = sorted(map(int, raw_input().strip().split()), reverse=True)
print sum(L[1::2])