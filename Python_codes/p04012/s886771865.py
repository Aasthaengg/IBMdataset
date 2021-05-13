# B - 美しい文字列
def main():
    import collections

    w = input()

    w_c = collections.Counter(w)

    for v in w_c.values():
        if v % 2 != 0:
            print('No')
            exit()
    else:
        print('Yes')
        

    
if __name__ ==  "__main__":
    main()