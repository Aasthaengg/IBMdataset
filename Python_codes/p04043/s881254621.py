ary = list(map(int, input().split()))
print('YES' if ary.count(5) == 2 and ary.count(7) == 1 else 'NO')