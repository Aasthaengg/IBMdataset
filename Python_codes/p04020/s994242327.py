N = int(input())
A = [int(input()) for _ in range(N)]

cnt = 0
remain = 0
for n in range(N):
    if A[n] == 0:
        remain = 0
        continue
    cnt += (A[n]+remain)//2 
    remain = (A[n]+remain)%2
print(cnt)