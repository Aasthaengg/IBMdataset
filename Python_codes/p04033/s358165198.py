def main():
    a, b = map(int, input().split())

    if a == 0 or b == 0:
        print("Zero")
    
    elif a < 0 and b > 0:
        print("Zero")

    elif a < 0 and b < 0:
        if abs(b - a + 1) % 2 == 1:
            print("Negative")
        else:
            print("Positive")

    elif a > 0 and b > 0:
        print("Positive")

if __name__ == "__main__":
    main()