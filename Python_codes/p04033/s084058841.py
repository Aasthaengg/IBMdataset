a, b = map(int, input().split())

if a < 0 and 0 < b:
    ans ='Zero'
elif b < 0:
    cnt = abs((b-a))+1
    if cnt%2 == 0:
        ans = 'Positive'
    else:
        ans = 'Negative'
elif 0 < a:
    ans = 'Positive'

print(ans)