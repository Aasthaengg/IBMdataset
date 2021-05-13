N = int(input())

sample = list(map(int, input().split()))
#sample = [100, 1, 2, 3, 14, 15, 58, 58, 58, 29]

max_idx = sample.index(max(sample))
sample.sort()
ans = 0
for i in range(len(sample)//2):
    ans += int(sample[i*2])
print(ans)