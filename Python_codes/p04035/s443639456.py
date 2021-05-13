INF = 10 ** 15
MOD = 10 ** 9 + 7 
def main():
    N,L = map(int,input().split())
    A = list(map(int,input().split()))
    point = -1
    for i in range(N - 1):
        if A[i] + A[i + 1] >= L:
            point = i + 1
            break
    if point == - 1:
        print('Impossible')
        return
    ans = []
    for i in range(point - 1):
        ans.append(i + 1)
    for i in range(N - 2,point - 1,-1):
        ans.append(i + 1)
    ans.append(point)
    print('Possible')
    print('\n'.join(map(str,ans)))
if __name__ == '__main__':
    main()