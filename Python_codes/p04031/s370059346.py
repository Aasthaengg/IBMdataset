N = int(input())

A = list(map(int,input().split()))

mean = sum(A)//len(A)

def std_div(mean, A):
    total = 0
    for x in A:
        total += (mean-x)**2
    return total

min1 = std_div(mean,A)
min2 = std_div(mean+1,A)

ans = min(min1,min2)
print(ans)
