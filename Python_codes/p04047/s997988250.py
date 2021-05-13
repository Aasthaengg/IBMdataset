N = int(input())
list = list(map(int, input().split()))
list.sort(reverse = True)

result = 0
for i in range(N):
    result += min(list[2 * i], list[2 * i + 1])

print(result)