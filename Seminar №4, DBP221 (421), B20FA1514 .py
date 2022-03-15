#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
import numpy as np
my_arr = np.arange(50,100)
my_arr


# In[2]:


#2
my_arr2 = np.zeros(10)
print(my_arr2)
my_arr3 = np.ones(10)
print(my_arr3)
my_arr4 = np.ones(10)*6
my_arr4


# In[3]:


#3
my_arr5 = np.arange(20,32)
data1 = np.arange(20,32)
a = np.reshape(data1,(3,4))
print(a)


# In[4]:


#4
a = np.zeros((3,3), int)
np.fill_diagonal(a,1)
print(a)


# In[5]:


#5
a = np.zeros((5,5), int)
np.fill_diagonal(a,(1,2,3,4,5))
print(a)


# In[6]:


#6
data3 = [[1,2,3,4], [6,5,4,8]]
arr6 = np.array(data3)
arr6
a = sum(map(sum,arr6))
print(a) #niit niilber
#baganiin niilber
print(np.sum(arr6, axis = 0))
#sum of each row
print(np.sum(arr6,axis=1))


# In[7]:


#7
Seasons = ["2015","2016","2017","2018","2019","2020","2021"]
Sdict = {"2015":0,"2016":1,"2017":2,"2018":3,"2019":4,"2020":5,"2021":6}
#player
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}
#salary
KobeBryant_Salary = [25000000,0,0,0,0,0,0]
JoeJohnson_Salary = [22309344,11000000,10254904,0,0,0,0]
LeBronJames_Salary = [22970500,30963450,33285709,35654150,37436858,39219566,41180000]
CarmeloAnthony_Salary = [22875000,24559380,26243760,2393887,2159029,2564753,2641691]
DwightHoward_Salary = [22359364,23500000,23500000,24256725,2564753,2564753,2641691]
ChrisBosh_Salary = [22192730, 23741060, 25289390, 26837720, 0,0,0]
ChrisPaul_Salary = [21468695, 22868827,24268959, 35654150, 38506482, 41358814, 30800000]
KevinDurant_Salary = [21971850,26540100,25000000,30000000,37199000,40108950,42018900]
DerrickRose_Salary = [21323252,2116955,416533,2176260,7317074,7682926,13445120]
DwayneWade_Salary = [20000000,23200000,15550000,2328652,2393887,2391886,2393887]
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])
#Games
KobeBryant_G = [66,0,0,0,0,0,0]
JoeJohnson_G = [81,78,55,0,0,0,1]
LeBronJames_G = [76,74,82,55,67,45,46]
CarmeloAnthony_G = [72,74,78,10,58,69,56]
DwightHoward_G = [71,74,81,9,69,69,47]
ChrisBosh_G = [31,32,0,0,0,0,0]
ChrisPaul_G = [74,61,58,58,70,70,58]
KevinDurant_G = [72,62,68,78,0,35,38]
DerrickRose_G = [66,64,25,51,50,50,26]
DwayneWade_G = [74,60,67,46,21,72,0]
Games = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])
##Minutes Played
KobeBryant_MP = [1861,0,0,0,0,0,0]
JoeJohnson_MP = [2705,1932,768,1840,1204,700,506]
LeBronJames_MP = [2706,2797,3026,1936,2318,1503,1693]
CarmeloAnthony_MP = [2527,2538,2504,294,1902,1691,1495]
DwightHoward_MP = [2279,2198,2462,230,1304,1194,691]
ChrisBosh_MP = [1755,0,0,0,0,0,0]
ChrisPaul_MP = [2419,1921,1844,1856,2205,2198,1914]
KevinDurant_MP = [2577,2070,2325,2698,0,1158,1387]
DerrickRose_MP = [2098,2080,420,1392,1300,1280,637]
DwayneWade_MP = [2257,1794,1534,1067,466,1886]
Minutes_Played = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])
### Points
#Points
KobeBryant_PTS = [1161,0,0,0,0,0,0]
JoeJohnson_PTS = [992,715,372,0,0,0,2]
LeBronJames_PTS = [1920,1954,2251,1505,1698,1126,1353]
CarmeloAnthony_PTS = [1573,1659,1261,134,895,924,767]
DwightHoward_PTS = [976,1002,1347,115,517,482,249]
ChrisBosh_PTS = [1010,0,0,0,0,0,0]
ChrisPaul_PTS = [1446,1104,1081,906,1232,1149,86]
KevinDurant_PTS = [2029,1555,1792,2027,0,943,0]
DerrickRose_PTS = [1080,1154,209,917,904,734,311]
DwayneWade_PTS = [1409,1096,765,1,0,0,0]
#Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])             
#Field Goals
KobeBryant_FG = [398,0,0,0,0,0,0]
JoeJohnson_FG = [377,273,146,0,0,0]
LeBronJames_FG = [737,736,857,558,643,422,509]
CarmeloAnthony_FG = [567,602,472,49,336,327,263]
DwightHoward_FG = [372,388,506,43,202,178,91]
ChrisBosh_FG = [358,0,0,0,0,0,0]
ChrisPaul_FG = [515,374,367,302,434,439,325]
KevinDurant_FG = [698,551,630,721,0,324,407]
DerrickRose_FG = [447,460,81,363,369,287,122]
DwayneWade_FG = [540,414,299,416,0,0,0]
Field_Goal = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])
#Field Goal Attempts
KobeBryant_FGA = [1113,0,0,0,0,0,0]
JoeJohnson_FGA = [859,626,360,0,0,0,0]
LeBronJames_FGA = [1416,1344,1580,1095,1303,823,976]
CarmeloAnthony_FGA = [1307,1389,1168,121,782,777,589]
DwightHoward_FGA = [600,613,911,69,277,303,150]
ChrisBosh_FGA = [767,0,0,0,0,0,0]
ChrisPaul_FGA = [1114,785,798,720,887,879,667]
KevinDurant_FGA = [1381,1026,1222,1383,0,603,784]
DerrickRose_FGA = [1048,977,186,753,753,611,274]
DwayneWade_FGA = [1183,955,682,960,0,0,0]
Field_Goal_attempt = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])


# In[8]:


Salary
print(Salary.sum(axis = 0))
print(Salary.sum(axis = 1))


# In[9]:


Games
print(Games.sum(axis = 1))
print(Games.sum(axis = 0))


# In[10]:


Points
print(Points.sum(axis = 0))
print(Points.sum(axis = 1))


# In[11]:


Minutes_Played 
print(Minutes_Played.sum(axis = 0))
print(Minutes_Played.sum(axis = 1))


# In[12]:


Field_Goal
print(Field_Goal.sum(axis = 0 ))
print(Field_Goal.sum(axis =1 ))


# In[13]:


Field_Goal_attempt
print(Field_Goal_attempt.sum(axis = 0))
print(Field_Goal_attempt.sum(axis = 1))


# In[ ]:




