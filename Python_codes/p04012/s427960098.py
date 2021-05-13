a = list(input())
even_number = [x for x in range(0,101,2)]
tmp_list = []
tmp_set = set(a)

tmp_list = [a.count(x) for x in tmp_set]
if all(x % 2 == 0 for x in tmp_list) == True:
    print("Yes")
else:
    print("No")