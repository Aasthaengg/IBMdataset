li = []
N = int(input())
li = list(map(int, input().split()))

li.sort(reverse=True)
re = sum(li[1::2])
print(re)