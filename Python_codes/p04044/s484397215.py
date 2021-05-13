N,L = map(int,input().split())
list1 = []
for l in range(N):
    list1.append(str(input()))
list1.sort()
print(''.join(list1))