#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Triangle():
    
    def __init__(self,s1,s2,s3):
       
        self.side1, self.side2, self.side3 = s1,s2,s3

class AreaOfTriangle(Triangle):
    
    def __init(self,s1,s2,s3):
        Triangle.__init__(self,s1,s2,s3)
        
    def getArea(self):
        s=(self.side1+self.side2+self.side3)*0.5
        area=(s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
        return area

s1=float(input("Enter side1: "))
s2=float(input("Enter side2: "))
s3=float(input("Enter side3: "))

Triangle1 = AreaOfTriangle(s1,s2,s3)
print("Area of Triangle is ",Triangle1.getArea())


# In[22]:


words=['word1','word2...','word3.','word4.....','word5..']
limit=int(input("Enter the limit for words: "))
result = []
for word in words:
    if len(word)>limit:
        result.append(word)

print("Following words have been filtered: ",result)


# In[24]:


def findLength(words):
    result=[]
    for word in words:
        result.append(len(word))
    return result

words=['word1','word2...','word3.','word4.....','word5..']
print("Following is the result: ",findLength(words))


# In[29]:


def findVow(ch):
    vow=['a','e','o','i','u','A','E','O','I','U']
    return ch in vow

character=input("Please enter a single character: ")
if findVow(character):
    print(character+" is a vowel")
else:
    print(character+" is not a vowel")


# In[ ]:





# In[ ]:




