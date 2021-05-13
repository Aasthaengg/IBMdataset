S = input()

NS = 'NS'
WE = 'WE'
answer = 'Yes'

if S.count('N') == 0 and S.count('S') != 0:
    answer = 'No'
elif S.count('N') != 0 and S.count('S') == 0:
    answer = 'No'

if S.count('W') == 0 and S.count('E') != 0:
    answer = 'No'
elif S.count('W') != 0 and S.count('E') == 0:
    answer = 'No'
        
print(answer)