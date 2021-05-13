
def main():
    num = int(input())
    data = list(map(int, input().split()))
    data.sort()
    ans = sum(data[::2])
    print(ans)



if __name__ == '__main__':
    main()
