#!/usr/bin/env python
# coding: utf-8

# In[1]:


def roots(a, b, c):
    disc = b**2 - 4 * a * c
    if(disc < 0):
        print("Root is complex: ", end='')
    return (-b + disc**0.5) / (2 * a), (-b - disc**0.5) / (2 * a)


# In[2]:


print(roots(1, 2, 1))
print(roots(3, 5, 2))
print(roots(5, 3, 4))
print(roots(-5, 4, -1))


# In[ ]:




