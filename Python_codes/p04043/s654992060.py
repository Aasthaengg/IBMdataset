# -*- coding: utf-8 -*-

if __name__ == "__main__":
    str_list = list(map(int, input().split()))
    if sum(str_list) == 17:
        print('YES')
    else:
        print('NO')
