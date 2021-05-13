from collections import Counter
W = Counter(list(input()))
Flag = True
for TW in W:
    if W[TW]%2!=0:
        Flag = False
        break
print(['No','Yes'][Flag])