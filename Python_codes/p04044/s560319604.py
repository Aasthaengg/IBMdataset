val1=list(map(int,input().split()))
val2=[input() for i in range(val1[0])]

val2.sort()
print("".join(val2))
