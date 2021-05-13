def main():
    a, b = map(int, input().split())

    if a == 0 or b == 0:
        print("Zero")
    elif a <= b < 0:
        if (b - a + 1) % 2 == 0:
            print("Positive")
        else:
            print("Negative")
    elif a < 0 < b:
        print("Zero")
    elif 0 < a <= b:
        print("Positive")


if __name__ == "__main__":
    main()
