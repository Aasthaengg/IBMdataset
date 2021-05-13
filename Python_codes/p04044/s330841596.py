s = [int(x) for x in input().split()]
s_list = []
for i in range(s[0]):
    s_list.append(input())

print(''.join(sorted(s_list)))
