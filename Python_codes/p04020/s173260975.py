N = int(input())
ans = 0
prev_A = -10
prev_card_num = 0
for i in range(1,N+1):
    A = int(input())
    ans += (prev_card_num + A)//2
    if prev_card_num == 1 and A == 0:
        prev_card_num = 0
    elif (prev_card_num+A)%2 == 1:
        prev_card_num = 1
        prev_A = i
    else:
        prev_card_num = 0
        prev_A = i
print(ans)