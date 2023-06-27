#!/usr/bin/env python
# coding: utf-8

# Q1. What is the role of try and exception block?
# 
# Ans. The role of a try and except block, also known as exception handling, is to handle and manage exceptions or errors that may occur during the execution of a program. Exceptions are unexpected events or conditions that disrupt the normal flow of a program.
# 
# Here's how a try and except block works:
# 
# The code inside the try block is executed. This is the portion of code where you anticipate an exception might occur.
# 
# If an exception occurs within the try block, the execution of the try block is immediately halted, and the program flow is transferred to the corresponding except block.
# 
# The except block contains the code that handles the exception. It specifies the actions to be taken when a specific exception is encountered. You can have multiple except blocks to handle different types of exceptions.
# 
# 

# In[1]:


# Q2. What is the syntax for a basic try-except block?

try:
    print (x)
except:
    print("there is no x")


# Q3. What happens if an exception occurs inside a try block and there is no matching except block?
# 
# Ans. If an exception occurs inside a try block and there is no matching except block to handle that specific exception, the program execution will be halted, and an error message will be displayed.
# 

# In[2]:


try:
    result = 10 / 0
except Exception as e:
    print("An error occurred:", str(e))


# In[3]:


# Q5. Can you have nested try-except blocks in Python? If yes, then give an example

x = 10
y = 0
try:
    print("outer try block")
    try:
        print("nested try block")
        print(x / y)
    except TypeError as te:
        print("nested except block")
        print(te)
except ZeroDivisionError as ze:
    print("outer except block")
    print(ze)


# In[4]:


# Q6. Can we use multiple exception blocks, if yes then give an example.


try:
    file_location = "my_file.txt"
    # (r = read, w = write )
    
    with open(file_location, "r") as file:
        contents  = file.read()
        
except FileNotFoundError:
    print("File you are looking for is not there")


# In[ ]:




