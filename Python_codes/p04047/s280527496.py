n, *l = map(int, open(0).read().split())
print(sum(min(sorted(l)[i*2:i*2+2]) for i in range(n)))