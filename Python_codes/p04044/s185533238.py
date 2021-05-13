N, L = map(int, input().split())
 
C = [input() for i in range(N)]
 
C.sort()
 
i=0
 
while i < N:
    print(C[i] , end ="")
    i += 1