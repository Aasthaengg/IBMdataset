
N,L = map(int,input().split())

a = list(map(int,input().split()))

flag = False
able = 0
for i in range(N-1):

    if a[i] + a[i+1] >= L:
        flag = True
        able = i
        break

if flag:

    print ("Possible")

    for i in range(able):
        print (i+1)

    for i in range(N-1-able):
        print (N-1-i)

    #print (able + 1)

else:
    print ("Impossible")
