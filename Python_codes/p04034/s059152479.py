def main():
    N, M = list(map(int, input().split()))
    proc_list = [list(map(lambda z: int(z) - 1, input().split())) for _ in range(M)]
    counter = [1] * N
    red_flag = [0] * N
    red_flag[0] = 1
    for from_box, to_box in proc_list:
        if red_flag[from_box] == 1:
            if counter[from_box] == 1:
                red_flag[from_box] = 0
            red_flag[to_box] = 1
        counter[from_box] -= 1
        counter[to_box] += 1
    print(sum(red_flag))


if __name__ == '__main__':
    main()