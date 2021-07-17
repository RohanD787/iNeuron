#!/usr/bin/env python
# coding: utf-8

# In[19]:


def compute():
        5/0
try:
    compute()
        
except(ArithmeticError):
    print("Invalid Operation: Division by 0")


# In[23]:


subjects=["Americans ","Indians "]
verbs=["play ","watch "]
objects=["Baseball ","Cricket "]

result=[subject+verb+obj for subject in subjects for verb in verbs for obj in objects]
print("Result is ",result)


# In[ ]:




