#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Жагсаалтад 'python', 'php', 'java' гэсэн утгуудыг хадгал. Жагсаалт дахь байрлалыг ашиглан эдгээр утга бүрийг хэвлэ.

list1=['python', 'php', 'java']
for element in list1:
    print(element)


# In[2]:


#2. 10 гишүүн бүхий тоон жагсаалт үүсгэ. Жагсаалтын нийлбэрийг давталт ашиглан хэвлэ.

list2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for element in list2:
    i = i + element 
print(i)


# In[5]:


#3. 5 гишүүн бүхий тоон жагсаалт үүсгэ.Жагсаалтын гишүүдийн үржвэрийг хэвлэх функц бич. Үр дүнг хэвлэ.

list3=[1,2,3,4,5]
def mutiple():
	i = 1 
	for element in list3:
		i = i*element
	print(i)

mutiple()


# In[12]:


#4. Өгөгдсөн тоон жагсаалтын 3 дахь элементийг сүүлийн сүүлийн элементтэй үржүүлэн үр дүнг буцаадаг функц бич.

list4 = [1,2,3,4,5,6,7,8,9]
a=list4[2]
b=list4[-1]
def lastdigit():
	print(a*b)

lastdigit()


# In[13]:


#5. Өгөгдсөн тоон жагсаалтаас хамгийн их болон хамгийн бага утгуудыг буцаах функц бич. Үр дүнг хэвлэ.

list5 = [1,2,3,4,5,6,7,8,9]
def list_return():
    min_utga = min(list5)
    max_utga = max(list5)
    print('Хамгийн их утга нь:', max_utga)
    print('Хамгийн бага утга нь:', min_utga)
    
list_return()


# In[14]:


#6. Өгөгдсөн жагсаалтаас хоёроос дээш оронтой, эхний болон төгсгөлийн тэмдэгтүүд нь хоорондоо адилхан гишүүн хэд байгааг тоолох функц бич.
#Жишээ: Оролт [abdba, abcd, 121 ], Гаралт 2

list6 = ['abba', 'tenet','kgkg', '505', '101', '101', '104', '1004', '1001']
def match(list6):
    a = 0
    for element in list6:
        if len(element) > 1 and element[0] == element[-1]:
            a += 1
    return a 
b = match(list6)
print(b)


# In[15]:


#7. Өгөгдсөн жагсаалтаас давхардсан утгуудыг арилгаж, хэвлэ.
#Жишээ: Оролт [abdba, abcd, 121, 121, abcd ], Гаралт [abdba, abcd, 121 ]

list7 = ['abba', 'tenet','kgkg', '505', '101', '101', '104', '1004', '1001']
new_list7 = set(list7)
print(list(new_list7))


# In[17]:


#8. Жагсаалт хоосон эсэхийг шалгах функц бич. Үр дүнг хэвлэ.

list8 = ['abba', 'tenet','kgkg', '505', '101', '101', '104']
def empty(list8):
    if len(list8) > 0:
        print('list хоосон биш байна.')
    elif len(list8) == 0:
        print('list хоосон байна.')
a = empty(list8)
print(a)


# In[18]:


#10. Тоон гишүүн бүхий tuple үүсгэ.

tuplex = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tuplex)


# In[19]:


#11. Tuple –д гишүүн нэмэх програм бич.

list11 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list11 = list(list11)
list11.extend([11,12,13,14])
list11 = tuple(list11)
print(list11)


# In[21]:


#12. Tuple –ийн 2 дахь элемент болон араасаа 2 дахь элементийг хэвлэ.

list12 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('2 дахь элемент:', list11[1])
print('Араасаа 2 дахь элемент:', list11[-2])


# In[ ]:


#13. Tuple –д гараас оруулсан утга байгаа эсэхийг шалгах програм бич.

set13 = ('1', '2', 'aba', '4', '5', '6', '7', '8')
utga = input('Ямар нэгэн утга оруулна уу: ')
if utga in set13:
    print('Оруулсан утга set-д байна.')
else:
    print('Оруулсан утга set-д байхгүй.')


# In[ ]:


#14. Өгөгдсөн Tuple –ийн бүх гишүүдийг давталт ашиглан хэвлэ.

list14 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for element in list14:
    print(element)


# In[ ]:


#15. 2 төрлийн set үүсгэн хооронд нь нэгтгэх програм бич.

def negdel():
    set15 = {1,2,3,4,5,6,7}
    set15_1 = {'banana', 'cherry'}
    negdel = set.union(set15, set15_1)
    print(negdel)
    
negdel()


# In[ ]:


#16. 2 төрлийн set үүсгэн аль алинд байгаа утгыг олох програм бич.

set16_1 = {'1', '2', 'aba', '4', '5', '6', '7', '8'}
set16_2 = {'4', '5', '8', '9', '3', '10', 'aba', '8'}

def intersection ():
    print('2 turliin set-d ali alind ni baigaa ugta:', set16_1 & set16_2)
    
intersection()


# In[ ]:


#17. Өгөгдсөн set-ийн уртыг ол.
print('17-р ажил:')

set17 = {1, 2, 3, 4, 5, 6, 7, 'cherry', 'banana'}
print(len(set17))


# In[ ]:


#18. Өгөгдсөн set-ээс гараас оруулсан утгыг устга.

set18 = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

set18.remove(input('set18-д байгаа 1-10 хооронд утга оруулна уу:'))
print(set18)


# In[ ]:


#19. Өгөгдсөн set-ийн бүх утгыг устга.

set19 = {1, 2, 3, 4, 5, 6, 7, 'cherry', 'banana'}
set19.clear()
print(set19)


# In[ ]:


#20. Өгөгдсөн set-ийг устга.

set19 = {1, 2, 3, 4, 5, 6, 7, 'cherry', 'banana'}
del set19


# In[ ]:


#21. Key, value нь тоон утга бүхий dictionary үүсгэж өсөх болон буурахаар эрэмбэл.

dict21 = { 
    10 : 2,
    2 : 3,
    5 : 4,
}

print('value утгаар нь key-г ихээс бага руу', sorted(dict21))
print('key утгаар нь value-g багаас их рүү', sorted(dict21.items()))


# In[ ]:


#22. Өгөгдсөн key нь dictionary –д байгаа эсэхийг шалгах програм бич.

dict22 = { 
    '10' : 2,
    '2' : 3,
    '5' : 4,
}

ugta = input('Утга оруулна уу: ')
a = dict22.keys()

if utga in a:
    print('Таны оруулсан утга байна.')
else:
    print('Таны оруулсан утга байхгүй байна.')


# In[ ]:


#23. Өгөгдсөн value нь dictionary –д байгаа эсэхийг шалгах програм бич.

dict23 = { 
    '10' : '2',
    '2' : '3',
    '5' : '4',
}

ugta = input('Утга оруулна уу: ')
a = dict22.values()

if utga in a:
    print('Таны оруулсан утга байна.')
else:
    print('Таны оруулсан утга байхгүй байна.')


# In[5]:


#24. For давталт ашиглан dictionary –ийн key, value –г хэвлэх програм бич.

dict24 = { 
    '10' : '2',
    '2' : '3',
    '5' : '4',
}
for key, value in dict24.items():
    print(key, ' : ', value)


# In[4]:


#25. Хоёр dictionary үүсгэж хооронд нь нэгтгэ.

dict25_1 = { 
    '10' : '2',
    '2' : '3',
    '5' : '4',
}
dict25_2 = {
    'bat' : 17,
    'mendee' : 20,
    'sod' : 5,
}
union = dict(dict25_1,**dict25_2)
print(union)


# In[3]:


#26. Dictionary –д байгаа value хооронд нь нэмэх програм бич.

dict26 = {
    'Содоо' : 13,
    'Тэмүүлэн' : 12,
    'Анхаа' : 2,
}

    
def sum_value(dict26):
    list = []
    for element in dict26:
        list.append(dict26[element])
    final = sum(list)
    return final

sum_value(dict26)


# In[ ]:




