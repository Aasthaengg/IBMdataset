def main():
    a, b, c = map(int, input().split())
    list = []
    list.append(a)
    list.append(b)
    list.append(c)

    if list.count(5) == 2 and list.count(7) == 1 :
        print("YES")
    else :
        print("NO")

if __name__ == '__main__':
    main()
