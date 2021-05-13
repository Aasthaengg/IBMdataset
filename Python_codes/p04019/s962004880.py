def main():
    S = input()
    if (S.count("N") >= 1 and S.count("S") >= 1 and S.count("E") == 0 and S.count("W") == 0)\
       or (S.count("N") == 0 and S.count("S") == 0 and S.count("E") >= 1 and S.count("W") >= 1)\
       or (S.count("N") >= 1 and S.count("S") >= 1 and S.count("E") >= 1 and S.count("W") >= 1):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()