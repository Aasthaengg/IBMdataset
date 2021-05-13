#!/usr/bin/env python
# coding: utf-8

# In[27]:


N,M = map(int, input().split())
xy = []
b = [1]*N
p = [False]*N
p[0] = True
for _ in range(M):
    x,y = map(int, input().split())
    b[x-1] -= 1
    b[y-1] += 1
    if p[x-1]:
        p[y-1] = True
    if b[x-1] == 0:
        p[x-1] = False


# In[28]:


ans = 0
for j in p:
    if j:
        ans += 1
print(ans)


# In[ ]:




