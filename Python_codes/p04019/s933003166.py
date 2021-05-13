# coding: utf-8
S = set(input())
i = {'N', 'S'}
j = {'W', 'E'}
k = {'N', 'S', 'W', 'E'}
if S == i or S == j or S == k:
    print('Yes')
else:
    print('No')