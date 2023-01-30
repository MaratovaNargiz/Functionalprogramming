#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Имя
Name=str(input("First name:")) 
#Фамилия
Surname= str(input("Last name:"))
#Возраст
Age=int(input("Age:"))
if(Age<=11):
 print("Children")
elif(Age>=12 and Age<=19):
 print("Teenager")
else:
 print("Аdult")
print((Name,Surname,Age))


# In[ ]:




