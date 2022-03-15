#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Өгөгдсөн утга нь палиндром эсэхийг шалгах функц бич.
a = input("Энд утга өгнө үү: ")
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Palindrome утга мөн.")
else:
    print("Palimdrome утга биш.")


# In[ ]:


#Өгөгдсөн жагсаалтаас том болон жижиг үсгүүдийг тоолох функц бич.
str = input("Энд утга өгнө үү: ")
tom = 0
jijig = 0
for i in range(len(str)):
    if(str[i]>='a' and str[i]<='z'):
        jijig = jijig + 1
    elif(str[i]>='A' and str[i]<='Z'):
         tom = tom + 1
print('Том үсгийн тоо: ', tom)
print('Жижиг үсгийн тоо: ', jijig)


# In[ ]:


#Жагсаалтын утгуудын үржвэрийг олох функц бич.

a = [1,2,3,4,5,6,7,8]
def multiple():
    i = 1
    for num in a:
        i = i*num
    print(i)
multiple()


# In[ ]:


#Өгөгдсөн тооны бактерал олох функц бич.

a = int(input("Enter a number: "))
factorial = 1
for i in range(1,num + 1):    
    factorial = factorial*i    
print("The factorial of",num,"is",factorial)  


# In[ ]:


#Өгөгдсөн жагсаалтыг урвуу болгох функц бич.

a = [1,2,3,4,5,6,7,8]
def reverse():
    a.reverse()
    print(a)
reverse()


# In[ ]:


#Жагсаалтын утгуудын нийлбэрийг олох функц бич.

a = [1,2,3,4,5,67,7]
def total():
    vol = 0
    for element in a:
        vol = vol+element
    print(vol)
total()


# In[ ]:


#Жагсаалтын давхардсан утгуудыг арилгах функц бич

a = ['1','2','2','3','ab','ab']
def erase():
    b = set(a)
    print(b)
erase()


# In[ ]:


#3 тооны хамгийн ихийг олдог функц бич.
def mx(a,b,c):
    if (a>=b) and (a>=c):
        max = a
    elif (b>=a) and (b>=c):
        max = b
    else:
        max = c
    return max

print(mx(10, 20, 30))


# In[ ]:




