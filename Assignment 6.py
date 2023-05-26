#!/usr/bin/env python
# coding: utf-8

# Q1. What are keywords in python? Using the keyword library, print all the python keywords.
# 
# Ans. Python Keywords are some predefined and reserved words in python that have special meanings. Keywords are used to define the syntax of the coding. The keyword cannot be used as an identifier, function, or variable name. 
# 
# To print the list of all keywords, we use "keyword. kwlist", which can be used after importing the "keyword" module, it returns a list of the keyword available in the current Python version. In the below code, we are implementing a Python program to print the list of all keywords

# In[1]:


import keyword 
print(keyword.kwlist)


# Q2. What are the rules to create variables in python?
# 
# Ans. Rules for Python variables:
# 
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# In[2]:


#for example 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Q3. What are the standards and conventions followed for the nomenclature of variables in
# python to improve code readability and maintainability?
# 
# Ans. In Python, variable and function names should be lowercase, with words separated by underscores. 
# 

# In[5]:


#for example
my_variable = "Hello, world!"
def my_function(): 
    print("This is my function.")


# Q4. What will happen if a keyword is used as a variable name?
# 
# Ans. You cannot use keywords as variable names. It's because keywords have predefined meanings.
#      keyword as a variable name in python because it will cause a syntax error. 
# 

# Q5. For what purpose def keyword is used?
# Ans. The def keyword is used to create, (or define) a function.
#     Use the keyword def to declare the function and follow this up with the function name.
#     Add parameters to the function: they should be within the parentheses of the function.
#     End your line with a colon. Add statements that the functions should execute

# Q.7. Give an example of the following conditions:
# (i) Homogeneous list
# (ii) Heterogeneous set
# (iii) Homogeneous tuple
# 
# Ans (i) Homogeneous list:
# A homogeneous list in Python is a list that contains elements of the same type. Here's an example of a homogeneous list that contains integers:

# In[1]:


numbers = [1, 2, 3, 4, 5]
print(numbers)


# (ii) Heterogeneous set :
#    A heterogeneous set in Python is a set that contains elements of different types. Here's an example of a heterogeneous set:
# 

# In[1]:


my_set = {1, 2.5, "hello", True}
print(my_set)


# (iii) Homogeneous tuple : 
#      A homogeneous tuple in Python is a tuple that contains elements of the same type. Here's an example of a homogeneous tuple that contains strings:

# In[2]:


names = ("Alice", "Bob", "Charlie", "David")
print(names)


# Q8. Explain the mutable and immutable data types with proper explanation & examples.
#  
# Ans. Mutable Data types : Mutable data types (changeable ) allow modifications to their values directly. This means that you can change their state or modify their elements without creating a new object. Mutable objects are unhashable and cannot be used as keys in dictionaries or elements in sets. Examples of mutable data types in Python include:
# 
# Lists: list
# Sets: set
# Dictionaries: dict
# 
#   Unmutable data types : Immutable data types(unchangeable) are those whose values cannot be modified after they are created. . Examples of immutable data types in Python include:
# 
# Numbers: int, float, complex.
# Strings: str.
# Tuples: tuple.

# In[4]:


#Mutable
lst = [1, 2, 1]  # list
my_set = {2, 8, 6}  # set
my_dict = {"name": "Alice", "age": 21}  # dictionary

lst.append(4)  
my_set.add(7)  
my_dict["age"] = 30

print(lst)  
print(my_set)  
print(my_dict)  

#unmutable 

x = 5  # integer
y = "Hello"  # string
z = (1, 2, 3)  # tuple

x += 1  
y += " World"  
z += (4,)  

print(x)  
print(y)  
print(z)



# Q9. Write a code to create the given structure using only for loop.
#   *
#  ***
# *****
# *******
# *********

# In[7]:


num_rows = 5
for i in range(num_rows):
   #spaces
    for j in range(num_rows - i - 1):
        print(" ", end="")
    
    for k in range(2*i + 1):
        print("*", end="")
    
    # next line 
    print()


# In[ ]:




