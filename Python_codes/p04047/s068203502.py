n = int(input())
li =  sorted(list(map(int,input().split())))

k=0
count =0
for i in range(n):
    count += li[k]
    k += 2

print(count)
