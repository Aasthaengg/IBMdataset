n, l = map(int, input().split())
aaa = list(map(int, input().split()))

max_i = 0
max_two_ropes = 0
for i in range(n - 1):
    two_ropes = aaa[i] + aaa[i + 1]
    if max_two_ropes < two_ropes:
        max_i = i
        max_two_ropes = two_ropes

if max_two_ropes < l:
    print('Impossible')
else:
    print('Possible')
    ans = list(range(1, max_i + 1))
    ans.extend(range(n - 1, max_i + 1, -1))
    ans.append(max_i + 1)
    print('\n'.join(map(str, ans)))
