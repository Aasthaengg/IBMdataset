N = int(input())
a = list(map(int,input().split()))

def minimize(list):
    min = 1000000
    for i in range(-100,101):
        num = 0
        for j in range(len(list)):
            num = num + (int(list[j]) - i)**2
        if min >= num:
            min = num
    return min

print(minimize(a))