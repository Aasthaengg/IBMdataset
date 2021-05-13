N = int(input())
A_list = list()
for i in range(N):
    A_list.append(int(input()))

ans = 0
#print(ans,A_list)  

#まず奇数を両端のどちらかに奇数があれば、それで打ち消す
if N > 1:
    if A_list[0]%2 == 1:
        if A_list[1] > 0:
            ans += 1
            A_list[0] -= 1
            A_list[1] -= 1

    #print(ans,A_list)  

    for i in range(1,N-1):
        if A_list[i]%2 == 1:
            if A_list[i-1]%2 == 1:
                ans += 1
                A_list[i] -= 1
                A_list[i-1] -= 1
            elif A_list[i+1] > 0:
                ans += 1
                A_list[i] -= 1
                A_list[i+1] -= 1
            elif A_list[i-1] > 0:
                ans += 1
                A_list[i] -= 1
                A_list[i-1] -= 1

        #print(ans,A_list)  
            
    if N >= 2:
        if A_list[N-1]%2 == 1:
            if A_list[N-2] > 0:
                ans += 1
                A_list[N-1] -= 1
                A_list[N-2] -= 1

    #print(ans,A_list)

#残ったのを自分同士で消す
for i in range(N):
    ans += A_list[i]//2
    A_list[i] = A_list[i]%2
    #print(ans,A_list)  
    
print(ans)
#print(A_list)