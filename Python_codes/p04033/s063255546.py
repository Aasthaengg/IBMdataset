def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print('Positive')
    elif (a > 0) ^ (b > 0) or a == 0 or b == 0:
        print('Zero')
    else:
        if (a - b) % 2 != 0:
            print('Positive')
        else:
            print('Negative')


if __name__ == '__main__':
    main()
