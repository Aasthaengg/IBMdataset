a = map(str, input().split())
three_num_list = list(a)

if '5' in three_num_list:
    three_num_list.remove('5')
    two_num_list = three_num_list
    if '5' in two_num_list and '7' in two_num_list:
        print('YES')
    else:
        print('NO')
else:
    print('NO')