n=int(input())

temp=0
cnt=0


for _ in range(n):
    a=int(input())
    hoge=min(a,temp)
    cnt+=hoge

    if a>hoge:
        cnt+=(a-hoge)//2
        temp=(a-hoge)-((a-hoge)//2)*2
    else:
        temp=0

print(cnt)


