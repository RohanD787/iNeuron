#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Question 1:

number=2000
result=[]
if number%7==0 and number%5!=0:
    result.append(number)
number=number+1

if number%7==0 and number%5!=0 :
    result.append(number)
number=number+1

while(number<=3200):
    if number%7==0 and number%5!=0 :
        result.append(number)
    number=number+7      

print(result)

#started the loop from first divisible number of 7 to reduce the number of iterations (number=number+7)


# In[19]:


#Question 2:

name=input("Please enter you first and last name: ")
space=name.find(" ")
print(name[space::],name[:space:])


# In[21]:


#Question 3:

radius=12.0/2.0 #Diameter is given as 12
V=(4.0/3.0)*3.14*radius*radius*radius  #formula is given
print("Area of Sphere is: ",V)


# In[ ]:




