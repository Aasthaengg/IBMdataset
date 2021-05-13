n = int(input())
l = list(map(int, input().split()))
l.sort()
print(sum([l[i] for i in range(0, 2 * n, 2)]))
