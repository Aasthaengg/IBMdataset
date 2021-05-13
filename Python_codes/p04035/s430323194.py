import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N, L = in_nn()
    A = in_nl()

    max_l = 0
    ind = -1
    for i in range(N - 1):
        t = A[i] + A[i + 1]
        if max_l < t:
            ind = i
            max_l = t

    if max_l >= L:
        print("Possible")
        for i in range(1, ind + 1):
            print(i)
        for i in range(N - 1, ind, -1):
            print(i)
    else:
        print("Impossible")


if __name__ == '__main__':
    main()
