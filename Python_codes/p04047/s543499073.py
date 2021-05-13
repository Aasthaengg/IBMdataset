if __name__ == '__main__':
    n =int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    count =0

    for i in range(n):
        count+=min(a[i*2],a[i*2+1])
    print(count)