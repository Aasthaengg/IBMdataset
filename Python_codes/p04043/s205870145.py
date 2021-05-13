# ABC158 A

def main():
    list = input().split()
    list.sort()
    if ''.join(list) == '557':
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
