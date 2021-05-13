def main():
    a, b, c = map(int, input().split())
    if a == 5 and b == 5 and c == 7:
        ans = 'YES'
    elif a == 5 and b == 7 and c == 5:
        ans = 'YES'
    elif a == 7 and b == 5 and c == 5:
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)


if __name__ == "__main__":
    main()
