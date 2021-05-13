# coding: utf-8

def main():
    a, b = map(int, input().split())
    ans = 'Positive'

    if a <= 0 and b >= 0:
        ans = 'Zero'
    elif b < 0:
        if (b - a) % 2 == 0:
            ans = 'Negative'

    print(ans)

if __name__ == "__main__":
    main()
