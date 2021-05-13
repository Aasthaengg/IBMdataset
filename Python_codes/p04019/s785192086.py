def main():
    s = input()

    n_cnt = s.count("N")
    w_cnt = s.count("W")
    s_cnt = s.count("S")
    e_cnt = s.count("E")

    if (n_cnt == 0 and s_cnt == 0) or (n_cnt > 0 and s_cnt > 0):
        if (w_cnt == 0 and e_cnt == 0) or (w_cnt > 0 and e_cnt > 0):
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
