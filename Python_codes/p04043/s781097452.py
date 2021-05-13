A,B,C = map(int, input().split())

list = sorted([A,B,C])

print('YES' if list == [5,5,7] else 'NO')