if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    b = 1

    if a[0]<= 0 and a[1]>=0:
        b=0
    elif a[1]<0:
        c = abs(a[0]-a[1])
        if c %2 ==0:
            b=-1


    if b >0:
        print("Positive")
    elif b ==0:
        print("Zero")
    else:
        print("Negative")