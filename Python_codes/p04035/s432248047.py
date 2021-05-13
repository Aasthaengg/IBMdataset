n,l,*a=map(int,open(0).read().split())
i=0
for a,b in zip(a,a[1:]):i+=1;a+b>=l>exit(print('Possible',*range(1,i),*range(n-1,i-1,-1)))
print('Impossible')