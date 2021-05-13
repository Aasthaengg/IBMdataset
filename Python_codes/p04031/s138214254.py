import statistics
n=int(input())
a=list(map(int,input().split()))
num=round(statistics.mean(a))
print(sum([(num-i)**2 for i in a]))