N = int(input())
A = [int(input()) for _ in range(N)]

cnt = 0
remain = 0
for a in A:
    if a == 0:
        remain = 0
        continue
    cnt += (a+remain)//2 
    remain = (a+remain)%2
print(cnt)