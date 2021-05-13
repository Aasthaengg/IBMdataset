N, L = map(int,input().split())
a_list = list(map(int,input().split()))

def equal_or_over_idx():
    for i in range(N-1):
        if a_list[i]+a_list[i+1] >=L:
            return i
    return -1

idx = equal_or_over_idx()
if idx == -1:
    print("Impossible")
else:
    print("Possible")
    for i in range(idx):
        print(i+1)
    for i in range(N-1,idx,-1):
        print(i)