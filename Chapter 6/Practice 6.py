#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('------------------------------')
print('  ******* HELLO WORLD ******  ')
print('------------------------------')
print('------------------------------')
print('  ******* HELLO WORLD ******  ')
print('------------------------------')


# In[2]:


def makeTitle():
    print('------------------------------')
    print('  ******* HELLO WORLD ******  ')
    print('------------------------------')

makeTitle()
makeTitle()

# In[3]:


def triArea(bottom, heigth):
    area = bottom * heigth /2
    return area

bottom = 10
heigth = 20
print('area of a triangle with bottom', bottom,
      'and heigth', heigth,
      'is', triArea(bottom, heigth))


# In[9]:


def triArea2(bottom ,heigth):
    area = bottom * heigth /2
    print('area of a triangle with bottom', bottom,
      'and heigth', heigth,
      'is', area)
bottom = 10
heigth = 20
triArea2(bottom , heigth)

# In[1]:


def count(a, b):
    result = a + b
    
a = 10
b = 20
count(a, b)
print(count(a,b))


# In[3]:


def count(a, b):
    result = a + b
    return result
    
a = 10
b = 20
count(a, b)
print(count(a, b))


# In[4]:


def myFunction():
    a = 20
    print(a)
    
a = 10
myFunction()
print(a)


# In[2]:


def isPythagoras(a, b, c):
    if a**2 + b**2 == c**2:
        print(True)
    else :
        print(False)
    
a = int(input("A Length : "))
b = int(input("B Length : "))
c = int(input("C Length : "))
isPythagoras(a, b, c)


# In[7]:


def starFormation1(n):
    for i in range(n+1):
        print('*'*i)

starFormation1(4)


# In[9]:


def starFormation2(n):
    for i in range(n, 0, -1):
        print('*'*i)
    
starFormation2(4)

# In[10]
def starFormat(n):
    remainder = n % 2
    if (remainder == 0):
        count = int(n / 2)
        starFormation1(count)
        starFormation2(count)
    else:
        count = int(n // 2)
        starFormation1(count)
        print("*"*(count+1))
        starFormation2(count)
n = int(input("Input n : "))
starFormat(n)


# In[1]:


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter a number : "))
print(factorial(n))


# In[4]:


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
def mutation(a, b):
    result = factorial(a)/factorial(b)
    print(result)

mutation(10, 7)


# In[5]:


def combination(a, b):
    result = factorial(a)/factorial(a-b)/factorial(b)
    print(result)
    
combination(5, 3)

