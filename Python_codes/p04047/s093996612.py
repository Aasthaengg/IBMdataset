n = int(input())
l = list(map(int, input().split()))
l.sort()
print(sum([l[i] for i in range(2*n) if i % 2 == 0]))