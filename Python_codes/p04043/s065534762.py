clause_list = list(map(int, input().split()))

for index, clause in enumerate(clause_list):
  if clause == 5:
    clause_list.pop(index)
    break

for index, clause in enumerate(clause_list):
  if clause == 7:
    clause_list.pop(index)
    break

for index, clause in enumerate(clause_list):
  if clause == 5:
    clause_list.pop(index)
    break

print('YES' if len(clause_list) == 0 else 'NO')
