#!/usr/bin/env python
# coding: utf-8

# In[1]:


Name=str(input("First name:")) 
Surname= str(input("Last name:"))
Age=int(input("Age:"))
if(Age<=11):
 print("Children")
elif(Age>=12 and Age<=19):
 print("Teenager")
else:
 print("Аdult")
print((Name,Surname,Age))


# In[ ]:




