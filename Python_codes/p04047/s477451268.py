n = int(input())
a = [int(i) for i in input().split()]
a.sort()
print(sum(a[0::2]))