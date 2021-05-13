num_list = [int(x) for x in input().split()]
if num_list == [5, 5, 7] or num_list == [5, 7, 5]  or num_list == [7, 5, 5]:
    print('YES')
else:
    print('NO')