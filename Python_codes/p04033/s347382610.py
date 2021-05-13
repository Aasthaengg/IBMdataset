N = tuple([int(j) for  j in input().split(' ')])

#0が含まれたら０
if N[0] <= 0 and N[1] >= 0:
    print("Zero")
elif N[0] < 0 and N[1] < 0:
    if (N[0] * - 1 - N[1] * - 1) % 2  == 0:
        print("Negative")
    else:
        print("Positive")
elif N[0] > 0 and N[1] > 0:
    print("Positive")
