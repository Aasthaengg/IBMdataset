n = int(input())
l = [int(i) for i in input().split()]
l.sort()
print(sum([l[i] for i in range(len(l)) if i%2 == 0]))
