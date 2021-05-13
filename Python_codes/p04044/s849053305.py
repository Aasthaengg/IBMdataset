# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n, l = [int(x) for x in input().rstrip().split(" ")]

    s_list = [input().rstrip() for _ in range(n)]
    s_list = sorted(s_list)
    print("".join(s_list))


if __name__ == "__main__":
    resolve()
