

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    answer = 0
    last = 0
    for _ in range(N):
        a = read_int()
        if a != 0:
            answer += (last+a)//2
            last = (last+a)%2
        else:
            last = 0
    return answer


if __name__ == '__main__':
    print(solve())
