def main():
    N,L = [int(n) for n in input().split()]
    A = [int(n) for n in input().split()]
    flg = False
    for i in range(N-1):
        if(A[i]+A[i+1] >= L):
            flg = True
            break
    if not flg:
        print("Impossible")
        return
    print("Possible")
    for j in range(1,i+1):
        print(j)
    for j in reversed(range(i+2,N)):
        print(j)
    print(i+1)
main()
