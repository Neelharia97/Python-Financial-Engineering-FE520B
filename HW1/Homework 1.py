#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Home Work 1
#Author : Neel Haria
#CWID : 10446034


# In[2]:


#Print
#1
a = "This is a string."
print(a)


# In[3]:


#2
string = "I'm a student"
print(string)


# In[4]:


#3
course_review = "This is an introduction course to Python for finance." "\n" "I am excited to learn Pandas and numpy during this course."
print(course_review)


# In[5]:


#Operator
#1
a = 100
b = 9
c = a+b
print(c)


# In[6]:


#2
print(a/b)


# In[7]:


#3
print(int(a/b))


# In[8]:


#4
print(a%b)


# In[9]:


#5
print(a**b)


# In[10]:


#6
flag = True
if a == b:
        flag = True
else:
        flag = False
    
print(flag)


# In[11]:


#7
if a>b:
    flag = True
else:
    flag = False
print(flag)


# In[12]:


#List
list_A = [1,1.0,1.1,3,1.5,2,2.2]
list_B = [2,2.2,23.0,50.0,4.0]
list_A.extend(list_B)
list_A


# In[13]:


list_A1 = [1,1.0,1.1,3,1.5,2,2.2]
list_A1.append(list_B)
list_A1


# In[14]:


list_A[1] = "FE520"
list_A


# In[15]:


list_A.remove("FE520")
list_A


# In[16]:


list_A[-1]


# In[17]:


list_A.pop()
list_A


# In[18]:


list_c = list_A[3:]
list_c


# In[ ]:





# In[19]:


#Dictionary
#1 
A = [1, 2, 3, 5, 10, 1, 4, 10, 11, 20, 50, 100]
B = []
for i in A:
    if i not in B:
        B.append(i)
    B.sort()
print(B)


# In[20]:


freq = {}
for i in A:
    if (i in freq):
        freq[i] += 1
    else:
        freq[i] = 1

for key,value in freq.items():
    print("%d : %d" % (key, value))


# In[21]:


#Loop
mylist  = [1, 2 , 4 , 9 , 17 , 25 , 63 ]
def loops(mylist, mynumber):
    mylist.append(mynumber)
    mylist.sort()
    print(mylist)
loops(mylist,13)

