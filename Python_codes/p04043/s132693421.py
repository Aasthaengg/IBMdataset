# coding: utf-8

input_ = input().split()

count_5 = 0
count_7 = 0

for i in input_:
    if i == '5':
        count_5 += 1
    elif i == '7':
        count_7 += 1

if count_5 == 2 and count_7 == 1:
    print('YES')
else:
    print('NO')
