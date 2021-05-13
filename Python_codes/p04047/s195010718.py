n = int(input())
l = [int(_) for _ in input().split()]
l.sort()
m = l[::2]
print(sum(m))