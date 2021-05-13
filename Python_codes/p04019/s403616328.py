s = list(set(list(input())))
ans = "Yes"

import collections
c = collections.Counter(s)

if c["N"] + c["S"] == 1 or c["W"] + c["E"] == 1:
    ans = "No"
    
print(ans)