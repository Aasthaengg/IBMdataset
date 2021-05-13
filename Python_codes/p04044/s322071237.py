N,L = map(int,input().split())
array = [input() for i in range(N)]
array.sort()
for i in array:
    print(i,end='')