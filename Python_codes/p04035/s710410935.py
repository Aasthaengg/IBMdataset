N, L = input().split()
N, L = int(N), int(L)

a = [0]*N

inputStr = input().split()
for i in range(N):
    a[i] = int(inputStr[i])

def check():
    for i in range(N-1):
        if(a[i]+a[i+1]>=L):
            return i
    return -1

b = check()

if(b==-1):
    print("Impossible")
else:
    print("Possible")
    for i in range(0,b):
        print(i+1)
    for i in range(b+1,N-1):
        print(N - (i-b))
    print(b+1)


