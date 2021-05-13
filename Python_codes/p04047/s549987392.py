input()
l = list(map(int, input().split()))
l.sort()
print(sum([v for i, v in enumerate(l) if i % 2 == 0]))