#!/usr/bin/env python
# coding: utf-8

# Q1. What exactly is []?
# 
# Ans. Ans : - [ ] is a empty list, like a =[]
# 
# Q2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# 

# In[1]:


spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
spam


# Q3. What is the value of spam[int(int('3' * 2) / 11)]?

# In[1]:


spam = ['a', 'b','c','d']
spam[int(int('3' * 2) / 11)] 
     


# Q4. What is the value of spam[-1]?

# In[2]:


spam = ['a', 'b','c','d']
spam[-1] 


# Q5. What is the value of spam[:2]?

# In[3]:


spam[:2] 


# *Let's pretend bacon has the list [3.14, 'cat' 11, 'cat' True] for the next three questions.*
# 
# 

# Q6.What is the value of bacon.index('cat')?

# In[5]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')


# Q7.How does bacon.append(99) change the look of the list value in bacon?

# In[8]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99)
bacon


# Q8. How does bacon.remove('cat') change the look of the list in bacon?

# In[9]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat') 
bacon


# Q9. What are the list concatenation and list replication operators?
# ( * ) is list replication operator ( + ) is list concatination operator

# In[11]:


list1 = [1,4]
list2 = [2,5]
v =list1+list2
print(v)


# In[14]:


#Replication operator
list1 = [2,7]
list1*3


# Q10. What is difference between the list methods append() and insert()?

# append() Appends object to the end of the list
# insert() Insert object before index

# In[15]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.append(99) 
bacon


# In[16]:


#inserting value in 3rd index
spam = [2, 4, 6, 8, 10]
spam.insert(2,'hello')
spam


# In[17]:


get_ipython().run_line_magic('pinfo', 'list')


# In[18]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat')
bacon


# In[19]:


bacon = [3.14, 'cat', 11, 'cat', True]
bacon.pop()
bacon
     


# Q12.Describe how list values and string values are identical.
# 
# Ans. (i)Both lists and strings can be passed to len()
#     (ii) Have indexes and slices
#     (iii)Can be used in for loops
#     (iv)Can be concatenated or replicated
#     (v) Can be used with the in and not in operators

# Q13. What's the difference between tuples and lists?
# 
# Lists : are mutable - they can have values added, removed, or changed. lists use the square brackets, [ and ]
# Tuples : are immutable; they cannot be changed at all. Tuples are written using parentheses, ( and )

# Q14. How do you type a tuple value that only contains the integer 42?

# In[20]:


tuple = (42,)
tuple
     


# Q15. How do you get a list value's tuple form? How do you get a tuple value's list form?

# In[25]:


l = tuple(l1)
l


# In[26]:


t1 = (3,4)
t = list(t1)
t


# Q16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# 
# Ans. They contain references to list values
# 
# 

# Q17. How do you distinguish between copy.copy() and copy.deepcopy()?
# 
# 
# Ans . The copy.copy() function will do a shallow copy of a list,
# The copy.deepcopy() function will do a deep copy of a list. only copy.deepcopy() will duplicate any lists inside the list
# 
# 
