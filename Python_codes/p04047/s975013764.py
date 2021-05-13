import sys

def main():
    sinputl = sys.stdin.readline

    num_skewer = int(sinputl().strip())
    input = [int(x) for x in sinputl().split()]
    input.sort()

    count = 0

    for i in range(num_skewer):
        count += input[i * 2]

    print(count)


if __name__ == "__main__":
    main()