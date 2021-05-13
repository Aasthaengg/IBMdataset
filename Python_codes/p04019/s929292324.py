s = list(set(list(input())))

if len(s)%2 == 0:
    if ("N" in s and"S" in s) or ("E" in s and "W" in s):
        print('Yes')
    else:
        print('No')
else:
    print('No')