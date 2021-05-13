# A - 和風いろはちゃんイージー
def main():
    abc = list(map(int, input().split()))
    c5 = 0
    c7 = 0

    for i in abc:
        if i == 5:
            c5 += 1
        elif i == 7:
            c7 += 1
    else:
        if c5 == 2 and c7 == 1:
            print('YES')
        else:
            print('NO')

            
if __name__ ==  "__main__":
    main()