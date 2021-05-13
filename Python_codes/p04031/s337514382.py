n = int(input())
a = sorted(map(int, input().split()))

ave = round(sum(a) / n)
ans = sum(map(lambda x: (ave - x) ** 2, a))
print(ans)