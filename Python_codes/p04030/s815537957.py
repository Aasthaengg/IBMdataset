#!/usr/bin/env python
# coding: utf-8

# In[5]:


s = input()


# In[6]:


ans = []
for i,w in enumerate(s):
    if w == "B" and len(ans) != 0:
        ans.pop(-1)
    elif w == "0" or w == "1":
        ans.append(w)
print("".join(ans))


# In[ ]:




