n = int(input())
list_int = list(map(int, input().split()))
ave0 = int(sum(list_int)/n)
ave1 = ave0 + 1
ave2 = ave0 - 1

list_cost0 = [(i-ave0)**2 for i in list_int]
list_cost1 = [(i-ave1)**2 for i in list_int]
list_cost2 = [(i-ave2)**2 for i in list_int]
print(min([sum(list_cost0), sum(list_cost1), sum(list_cost2)]))