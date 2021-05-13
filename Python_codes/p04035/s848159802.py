import math

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

#a = list(map(int, input().split()))

#####################################


#4:25
n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
maxv=0
maxid=-1
for i in range(n-1):
    if(maxv<a[i]+a[i+1]):
        maxv=a[i]+a[i+1]
        maxid=i+1

if(maxv<k):
    print("Impossible")
    exit()
print("Possible")
for j in range(maxid-1):
    print(j+1)
    
for j in range(n-maxid-1):
    print(n-1-j)
    
print(maxid)