import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    use = -1
    for i in range(N-1):
        if a[i]+a[i+1] >= M:
            use = i
            break
    
    if use == -1:
        print("Impossible")
    else:
        print("Possible")
        for j in range(i):
            print(j+1)
        for j in range(N-1,i,-1):
            print(j)

if __name__ == "__main__":
    main()