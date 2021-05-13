n,_=map(int,input().split())
l=''.join(sorted([''.join(sorted(input().split())) for _ in range(n)]))
print(l)
