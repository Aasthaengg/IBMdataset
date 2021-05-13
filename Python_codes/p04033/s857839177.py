def main():
    a, b = map(int, input().split())

    if a > 0:
        print("Positive")
        return

    if b > 0 and a <= 0:
        print("Zero")
        return

    print("Positive" if(b - a + 1) % 2 == 0 else "Negative")


if __name__ == '__main__':
    main()
