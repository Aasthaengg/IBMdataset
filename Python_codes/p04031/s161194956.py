N = int(input())
a = list(map(int, input().split()))
min_val = None
stacks = 0

for i in range(-100, 101):
    cost_stack = 0
    for j in range(len(a)):
        cost_stack += (a[j] - i) ** 2
        
    if min_val == None:
        min_val = cost_stack
    elif cost_stack < min_val:
        min_val = cost_stack

print(min_val)
