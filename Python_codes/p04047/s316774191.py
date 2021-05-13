n = int(input())
li_l = list(map(int, input().split()))

print(sum(sorted(li_l, reverse=True)[1::2]))
