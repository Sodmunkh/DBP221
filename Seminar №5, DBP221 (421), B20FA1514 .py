#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Гараас оруулсан n тоо хүртэл “*” тэмдэгтийг мөр бүрд хэвлэх функц бич
n = int(input())
k = 1 
for i in range(n + 1):
    k ="*"*1
    i += 1
    print(k)


# In[19]:


# Гараас оруулсан n тоо хүртэл “*” тэмдэгтийг жагсаалтын мөр бүрд хэвлэх функц бич.
def pypart(n):
    mylist =[]
    for i in range(1, 1+n):
        mylist.append("*"*i)
    print("\n".join(mylist))
    n = int(input())
pypart(n)


# In[20]:


#Дараах жагсаалтаас хамгийн их, хамгийн бага key-г авах функц бич.
a_dictionary = {'Bat': 18, 'Oyun': 22, 'Dulam': 21, 'Suren': 20}
max_key = max(a_dictionary, key=a_dictionary.get)
min_key = min(a_dictionary, key=a_dictionary.get)
a = (max_key, min_key)
print(a)


# In[22]:


# np.arange(1-1000) массив үүсгэ. Тухайн массиваас 3 эсвэл 7 –д хуваагдах тоонуудын нийлбэрийг ол.
import numpy as np
x = np.arange(1, 1000)
n = x[(x % 3 == 0) | (x % 7 == 0)]
print(n)
print(n.sum())


# In[ ]:




