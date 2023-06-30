#!/usr/bin/env python
# coding: utf-8

# 1. What does an empty dictionary's code look like?

# In[1]:


dict = {}
type(dict)
     


# 2. What is the value of a dictionary value with the key 'foo' and the value 42?

# In[2]:


{'foo':42}


# 3.What is the most significant distinction between a dictionary and a list?
# 
# 
# List - items in list are Ordered
# Dictionary : iten in dictionary are unordered

#  5.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# In[4]:


spam ={'cat':100}
'cat' in spam
     


# In[5]:


'cat' in spam.keys()


# In[6]:


spam ={'cat':100}
'cat' in spam.values()


# 7.What is a shortcut for the following code?
# 

# In[9]:


spam ={'cat':100}
spam.setdefault('Doll','pink')
spam


# 8.How do you 'pretty print' dictionary values using which module and function?

# In[10]:


import pprint
dct = [ {'Name': 'Shruti', 'Age': '20', 'Country': 'India'},
  {'Name': 'Ashia', 'Age': '26', 'Country': 'China'},
  {'Name': 'Joe', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Chumlee', 'Age': '35', 'Country': 'USA'}
]


# In[11]:


pprint.pprint(dct)
     


# In[ ]:





# In[ ]:




