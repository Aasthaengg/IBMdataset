# -*- coding: utf-8 -*-

def main():

    w = input()
    setW = set(w)
    listW = list(w)
    n = len(listW)

    for i in setW:
        if listW.count(i) % 2 == 1:
            ans = 'No'
            break

        else:
            ans = 'Yes'

    print(ans)

if __name__ == "__main__":
    main()