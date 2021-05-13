from collections import Counter


def main():
    w = list(input())
    w_counter = Counter(w)
    ans = 'Yes'
    for key, value in w_counter.items():
        if value % 2 != 0:
            ans = 'No'
            break
    print(ans)


if __name__ == "__main__":
    main()
