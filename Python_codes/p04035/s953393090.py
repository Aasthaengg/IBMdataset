N, L = map(int, input().split())
a = list(map(int, input().split()))

#最後に切るものを決める
i = 0
flag = False
while i < N - 1:
    if a[i] + a[i + 1] >= L:
        flag = True
        break
    i += 1

if not flag:
    print ('Impossible')
else:
    print ('Possible')
    for j in range(i):
      print (j + 1)
    for j in range(N - 1, i, -1):
      print (j)
