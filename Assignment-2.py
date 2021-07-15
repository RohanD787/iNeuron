#!/usr/bin/env python
# coding: utf-8

# In[13]:


middle_row=int(input("Enter the number of stars in largest row: "))
for i in range(middle_row):
    for j in range(i):
      print("*",end=" ")
    print()
for i in range(middle_row,0,-1):
    for j in range(i,0,-1):
      print("*",end=" ")
    print()


# In[26]:


word=input("Enter any word: ")
strlen=len(word)
word[strlen::-1]


# In[ ]:





# In[ ]:




