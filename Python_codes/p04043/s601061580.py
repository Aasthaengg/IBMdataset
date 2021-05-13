def main():
    abc = ''.join(sorted(input().replace(' ', '')))
    print('YES' if abc == '557' else 'NO')


if __name__ == '__main__':
    main()
