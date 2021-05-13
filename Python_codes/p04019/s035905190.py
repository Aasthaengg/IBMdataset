import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    go_back_home = True
    if "N" in S:
        if "S" not in S:
            go_back_home = False
    if "S" in S:
        if "N" not in S:
            go_back_home = False
    if "W" in S:
        if "E" not in S:
            go_back_home = False
    if "E" in S:
        if "W" not in S:
            go_back_home = False

    ans = "Yes" if go_back_home else "No"
    print(ans)


if __name__ == "__main__":
    main()
