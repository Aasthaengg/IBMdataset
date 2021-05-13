def main():
    a, b = map(int, input().split())
    if a > 0:
        print('Positive')
    elif a <= 0 and b >= 0:
        print('Zero')
    else:
        cnt = b - a + 1
        if cnt%2 == 0:
            print('Positive')
        else:
            print('Negative')

if __name__ == "__main__":
    main()
