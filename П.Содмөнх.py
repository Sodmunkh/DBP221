#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd
pd.__version__


# In[20]:


data0 = pd.read_excel("Бие даалт - 1.xlsx", sheet_name = 'Ирц')
data1 = pd.read_excel("Бие даалт - 1.xlsx", sheet_name = 'Семинар')
data2 = pd.read_excel("Бие даалт - 1.xlsx", sheet_name = 'Шалгалт')
data3 = pd.read_excel("Бие даалт - 1.xlsx", sheet_name = 'Бие даалт')
data4 = pd.read_excel("Бие даалт - 1.xlsx", sheet_name = 'Хүмүүжил хандлага')
data5 = pd.read_excel("Бие даалт - 1.xlsx", sheet_name = 'Нэмэлт оноо')
data6 = pd.read_excel("Бие даалт - 1.xlsx", sheet_name = 'Нийт')


# In[21]:


#1.Ирц
data0_cl = data0.replace(['и','т'],[1,0])
data0_sum = data0_cl.iloc[:, 4:].sum(axis = 1)
data0_pt = ((data0_sum / 32)*10).round()


# In[22]:


#2.Семинар
data1_cl = data1.fillna(0)
data1_sum = data1_cl.iloc[:, 4:].sum(axis = 1)
data1_pt = (data1_sum * (25/19)).round()


# In[23]:


#3.Шалгалтууд
data2_cl = data2.fillna(0)
data2_sum = (data2_cl.iloc[:, 4:].sum(axis = 1)).round()


# In[24]:


#4,5.Бие Даалтууд
data3_cl = data3.fillna(0)
data3_sum = (data3_cl.iloc[:, 4:].sum(axis = 1)).round()


# In[25]:


#6,7,8,9.Хүмүүжил хандлагууд
data4_cl = data4.fillna(0)
data4_sum = (data4_cl.iloc[:, 4:].sum(axis = 1)).round()


# In[26]:


#10.Нэмэлт оноо
data5_cl = data5.fillna(0)
data5_sum = (data5_cl.iloc[:, 4:].sum(axis = 1)).round()


# In[27]:


#Оюутны нэрс болон код
student = data6.iloc[:-1, 2:4]


# In[28]:


#Нийт нийлбэр
niilber = (data0_pt + data1_pt + data2_sum + data3_sum + data4_sum + data5_sum).round()


# In[29]:


niit = pd.DataFrame({
    'Ирц' : data0_pt,
    'Семинар' : data1_pt,
    'Шалгалт' : data2_sum,
    'Бие Даалт' : data3_sum,
    'Хүмүүжил хандлага' : data4_sum,
    'Нэмэлт оноо' : data5_sum,
    'Нийт оноо' : niilber
})


# In[30]:


#Бүхэл dataframe болгосон нь
niit1 = pd.concat([student, niit], axis = 1)


# In[31]:


conditions = [
    (niit1['Нийт оноо'] >= 96) & (niit1['Нийт оноо'] <=100),
    (niit1['Нийт оноо'] >= 90) & (niit1['Нийт оноо'] <=95),
    (niit1['Нийт оноо'] >= 87) & (niit1['Нийт оноо'] <=89),
    (niit1['Нийт оноо'] >= 83) & (niit1['Нийт оноо'] <=86),
    (niit1['Нийт оноо'] >= 80) & (niit1['Нийт оноо'] <=82),
    (niit1['Нийт оноо'] >= 77) & (niit1['Нийт оноо'] <=79),
    (niit1['Нийт оноо'] >= 73) & (niit1['Нийт оноо'] <=76),
    (niit1['Нийт оноо'] >= 70) & (niit1['Нийт оноо'] <=72),
    (niit1['Нийт оноо'] >= 67) & (niit1['Нийт оноо'] <=69),
    (niit1['Нийт оноо'] >= 63) & (niit1['Нийт оноо'] <=66),
    (niit1['Нийт оноо'] >= 60) & (niit1['Нийт оноо'] <=62),
    (niit1['Нийт оноо'] >=  0) & (niit1['Нийт оноо'] <=59)
]


# In[32]:


values = ['A', 'A-',
          'B+', 'B', 'B-',
          'C+', 'C', 'C-',
          'D+', 'D', 'D-',
          'F']


# In[33]:


gpa = ['4.0', '3.7',
          '3.4', '3.0', '2.7',
          '2.4', '2.0', '1.7',
          '1.3', '1.0', '0.7',
          'Унасан']


# In[34]:


niit1['Үнэлгээ'] = np.select(conditions, values)
niit1['Голч дүн'] = np.select(conditions, gpa)


# In[35]:


niit1


# In[ ]:





# In[ ]:




