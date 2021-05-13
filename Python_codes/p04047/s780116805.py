n = int(input())
num_list = [ int(v) for v in input().split() ]
print(sum(sorted(num_list)[::2]))