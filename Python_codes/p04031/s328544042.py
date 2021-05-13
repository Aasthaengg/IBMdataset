def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    sum_A = sum(A)
    left, right = sum_A // N, sum_A // N + 1
    loss_1 = sum([(a - left) ** 2 for a in A])
    loss_2 = sum([(a - right) ** 2 for a in A])
    if loss_1 < loss_2:
        print(loss_1)
    else:
        print(loss_2)


if __name__ == '__main__':
    main()