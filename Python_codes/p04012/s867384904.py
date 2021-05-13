
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    w = input().rstrip()

    import string

    result = {alp: True for alp in string.ascii_lowercase}

    for c in w:
        result[c] = not result[c]

    if all(result.values()):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    resolve()
