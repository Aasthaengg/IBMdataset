n=int(input())
l=sorted(list(map(int, input().split())))
ll=l[::2]
print(sum(ll))