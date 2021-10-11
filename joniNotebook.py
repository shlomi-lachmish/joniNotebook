#!/usr/bin/env python
# coding: utf-8

# Location is combinationnn of string & number.
# e.g. "B5"
# 
# first string char stands for row B=>second row from the top
# "A" in ascii is 65  and "F"
# 
# while the second int char stands for the column 5=> 5th column

# In[15]:


print(ord("A"), ord("F"))


# In[16]:


chr(ord("A")+1)


# We will definne 4 move functions 
# * moveUp
# * moveRight
# * moveDown
# * moveLeft

# In[68]:


location ="C3"


# In[69]:


def moveUp(location):
    print(ord(location[0]))
    if ord(location[0]) > 65:
        newRow = chr(ord(location[0])-1)
        location = newRow+location[1]
    else:
        print("you cannot go up from this location")
    return location


# In[72]:


location = moveUp(location)
print(location)


# In[73]:


def moveRight(location):
    print(ord(location[1]))
    if int(location[1]) < 7:
        newCoumn = int(location[1])+1
        location = location[0]+str(newCoumn)
    else:
        print("you cannot go right from this location")
    return location


# In[78]:


location = moveRight(location)
print(location)

