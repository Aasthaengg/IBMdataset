n,l = map(int,input().split())
arr = list(map(int,input().split()))

key = 0
flag = False
for i in range(n-1):
    if arr[i] + arr[i+1] >= l:
        key = [i,i+1]
        flag = True
        break

# print(key)
if flag:
    print("Possible")
    for i in range(key[0]):
        print(i+1)
    temp = []
    for i in range(key[1]+1,n):
        temp.append(i)
    temp.reverse()
    for t in temp:
        print(t)
    print(key[1])

else:
    print("Impossible")


