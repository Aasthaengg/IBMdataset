n, s = map(int, raw_input().split())
values = list(map(int, raw_input().split()))
found = False
for pos in range(n - 1):
    if values[pos] + values[pos + 1] >= s:
        found = True
        break
if not found:
    print('Impossible')
    import sys
    sys.exit()
    
result = (n - 1) * [ None ]
result[n - 2] = pos + 1
ix = n - 3
for i in range(pos - 1, -1, -1):
    result[ix] = i + 1
    ix -= 1
for i in range(pos + 1, n - 1):
    result[ix] = i + 1
    ix -= 1
print('Possible')
print('\n'.join(map(str, result)))
