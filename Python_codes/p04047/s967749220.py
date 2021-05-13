n=int(input())
L=sorted(list(map(int, input().split())))

all_sum=0
for i in range(0,2*n,2):
    all_sum+=L[i]
print(all_sum)