#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd


# In[19]:


pd.__version__


# In[20]:


data0 = pd.read_excel("Week7_Store Data Sample.xlsx", sheet_name = "Sheet1")
data0


# In[21]:


#1 Эхний 10 мөрийг сонгож авна уу.
data1 = data0.iloc[:11]
data1


# In[22]:


#2 78-88 дугаар мөрөнд байгаа мэдээллээс Product Name, Sales багануудыг харуулна уу.
data2 = data0.loc[78:88,['Product Name', 'Sales']]
data2


# In[23]:


#3 Quantity болон Sales баганыг сонгож авна уу.
data3 = data0.T
data3 = data3.loc[['Quantity','Sales']]
data3.T


# In[24]:


#4 Quantity болон Sales баганын нийлбэрүүдийг харуулна уу.
data4 = data0['Quantity'] + data0['Sales']
data4


# In[25]:


#5 Product Name баганыг сонгож авна уу.
data5 = data0.T
data5 = data5.loc[['Product Name']]
data5.T


# In[26]:


#6 Product Name баганын давхардаагүй утгуудыг харуулна уу.
data6 = data0['Product Name'].unique()
data6


# In[27]:


#7 Product Name баганын давхардаагүй утгууд нийт хэд байгааг тоолж харуулна уу.
data7 = data0['Product Name'].nunique()
data7


# In[28]:


#8 Product Name баганын давхардсан утгуудыг харуулна уу.
data8 = data0.['Product Name'].merge()
data8


# In[30]:


#9 Order ID баганын давхардаагүй утгууд нийт хэд байгааг тоолж харуулна уу.
data9 = data0['Order'].unique()
data9


# In[ ]:




