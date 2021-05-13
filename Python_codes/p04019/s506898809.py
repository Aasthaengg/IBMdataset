#!/usr/bin/env python
# coding: utf-8

# In[7]:


S = input()


# In[8]:


s_set = set(S)
if "S" in s_set and "N" in s_set:
    if "E" in s_set and "W" in s_set:
        print("Yes")
    elif "E" in s_set or "W" in s_set:
        print("No")
    else:
        print("Yes")
elif "S" in s_set or "N" in s_set:
    print("No")
else:
    if "E" in s_set and "W" in s_set:
        print("Yes")
    elif "E" in s_set or "W" in s_set:
        print("No")
    else:
        print("Yes")


# In[ ]:




