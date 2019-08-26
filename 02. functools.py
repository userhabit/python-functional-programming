#!/usr/bin/env python
# coding: utf-8

# # functools
# ##### singledispatch

# In[5]:


from functools import singledispatch

@singledispatch
def fn(x):
    print(x)

@fn.register(int)
def _(x):
    print("Integer:", x)

@fn.register(str)
def _(x):
    print("String:", x)

@fn.register(float)
def _(x):
    print("Float:", x/2)


# In[6]:


fn('1')


# In[7]:


fn(1)


# In[ ]:




