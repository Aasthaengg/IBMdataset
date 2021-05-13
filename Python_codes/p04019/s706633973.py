# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    se = input().rstrip()

    S = "S" in se
    N = "N" in se
    E = "E" in se
    W = "W" in se

    if (S ^ N) or (E ^ W):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    resolve()
