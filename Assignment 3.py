#!/usr/bin/env python
# coding: utf-8

# Q1. Why are functions advantageous to have in your programs?
# 
# Ans. Functions enhance code organization, readability, reusability, and maintainability, making your programs more efficient, scalable, and easier to work with in the long run.
# Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.

# Q2. When does the code in a function run:when it's specified or when it's called?
# 
# Ans . Code in the function runs when the function is called
# 
# 

# Q3. What statement creates a function?
# 
# Ans. The def statement defines (i.e. creates) a function.

# In[2]:


#for example
def my_func():
    pass


# Q4. What is the difference between a function and a function call?

# In[3]:


#function
def my_func(): 
    pass 
#function call
my_func() 


# A function is a block of code that performs a specific task or a set of instructions. It is a reusable component that 
# encapsulates a particular functionality within a program.
# 
# A function call is what moves the program execution into the function, and the function call evaluates to the function's return value.

# Q5. How many global scopes are there in a Python program
# 
# Ans .There's only one global Python scope per program execution. This scope remains in existence until the program terminates , and a local scope is created whenever a function is called.

# Q6. What happens to variables in a local scope when the function call returns?
# 
# Ans. When a function returns, the local scope is destroyed.

# Q7. What is the concept of a return value? Is it possible to have a return value in an expression?
# 
# Ans. A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.
# 
# Q8. If a function does not have a return statement, what is the return value of a call to that function?
# 
# Ans. If the funtion does not have a return statement it will not return anything.
# 
# Q9. How do you make a function variable refer to the global variable?
# 
# Ans. To make function variable as a global variable you can use the global keyword to declare which variables are global.
# 
# Q10. What is the data type of None?
# 
# Ans . The data type of None is NoneType.
# 
# Q12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 
# Ans .import spam
# spam.bacon()
# 
# 
