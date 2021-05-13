w = list(input())
j = 0
ans = 0

if(len(w)%2 != 0):
    print('No')
else:
    for i in range(len(w)):
        j = w.count(w[i])
        if(j%2 == 0 and i == len(w)-1):
            print('Yes')
            break
        elif(j%2 != 0):
            print('No')
            break