N = int(input())

ans = 0
List = []
for i in range(N):
    A = int(input())
    List.append(A)
    
def func(a, b):
    ret = 0
    for i in range(a, b + 1):
        ret += List[i] // 2
        if List[i] % 2 and i != b:
            List[i + 1] -= 1
            ret += 1
    return ret

left = 0
for right in range(N):
    if List[right] == 0:
        ans += func(left, right - 1)
        left = right + 1
    
ans += func(left, N - 1)

print(ans)