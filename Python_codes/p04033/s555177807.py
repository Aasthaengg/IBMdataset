def main():
    a, b = map(int, input().split())
    if a * b <= 0:
        print('Zero')
    elif a > 0 or (abs(b - a) + 1) % 2 == 0:
        print('Positive')
    else:
        print('Negative')

if __name__ == '__main__':
    main()
