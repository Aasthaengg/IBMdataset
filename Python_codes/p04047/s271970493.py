n = int(input())
lst = list(map(int,input().split()))
lst.sort()
s = sum(lst[0::2])
print(s)
