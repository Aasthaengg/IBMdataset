def solve(A,L):
    N = len(A)
    for i in range(N-1):
        if A[i]+A[i+1] >= L:
            pro = i
            break
    else:
        return None

    res = list(range(i))+list(reversed(range(i+1,N-1)))+[i]
    return res


if __name__ == '__main__':
    N,L = map(int,input().split())

    A = list(map(int,input().split()))

    res = solve(A,L)
    if res is None:
        print('Impossible')
    else:
        print('Possible')
        print(*(v+1 for v in res), sep='\n')