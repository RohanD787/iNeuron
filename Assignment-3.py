#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[26]:


import functools
def sqr(n,m):
    r=n*m
    print(f"{m}X{n}={r}")
    return r
l=[2,3,4,5,6]
functools.reduce(sqr, l)


# In[29]:


def myreduce(funct,iterable,init = None):
    iterable=iter(iterable)
    if init==None:
        result=next(iterable)
    else:
        result=init
    for element in iterable:
        result= funct(result,element)
    return result
        

myreduce(sqr,l)


# In[41]:


def myfilter(funct,iterable,init=None):
    iterable=iter(iterable)
    if init==None:
        result=next(iterable)
    else:
        result=init
    for element in iterable:
        if funct(element)==True:
            result=element
    return result

def even(num): 
    if num%2==0:
        print(num)
        return True
    else:
        return False
   

l=[17,5,88,9,6,22,54]
myfilter(even,l)


# In[80]:


list1=['x','y','z']
list2=[1,2,3,4,5,6,7,8]

result1=[ch*i for ch in list1 for i in range(1,4)]
result2=[ch*i for i in range(1,4) for ch in list1]

result3=[list2[i:i+4] for i in range(4)]



# In[ ]:





# In[5]:


result4=[list2[i:i+1] for j in range(4) for i in range(j,j+4)]
result4


# In[7]:


result5=[(list2[j],list2[i]) for i in range(len(list2)) for j in range(len(list2))]
result5


# In[ ]:




