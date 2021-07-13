#!/usr/bin/env python
# coding: utf-8
# In[7]:


def sumIt(*data):
    output = 0
    for i in data:
        output += i
    print(output)
    
sumIt(5, 10, 4, 9, 30, 16, 2, 11)
sumIt(81, 98, 12, 83, 45, 77, 69, 30, 56)


# In[9]:


def average(*data):
    output = 0
    for i in data:
        output += i
    output /= len(data)
    print(output)

average(5, 10, 4, 9, 30, 16, 2, 11)
average(81, 98, 12, 83, 45, 77, 69, 30, 56)


# In[13]:


def maxIt(*data):
    print(max(data))
    
maxIt(5, 10, 4, 9, 30, 16, 2, 11)
maxIt(81, 98, 12, 83, 45, 77, 69, 30, 56)


# In[12]:


def minIt(*data):
    print(min(data))
    
minIt(5, 10, 4, 9, 30, 16, 2, 11)   
minIt(81, 98, 12, 83, 45, 77, 69, 30, 56)


# In[ ]:




