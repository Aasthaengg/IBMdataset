n = int(input())
li = [int(x) for x in input().split()]

def skews(n,li):
    
    li = sorted(li)
    li = [l for i,l in enumerate(li) if i%2==0] 
    return sum(li)


print(skews(n,li))
