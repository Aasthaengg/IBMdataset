from typing import List


def answer(n: int, l: int, s: List[str]) -> str:
    return ''.join(sorted(s))


def main():
    n, l = map(int, input().split())
    s = [input() for _ in range(n)]
    print(answer(n, l, s))


if __name__ == '__main__':
    main()