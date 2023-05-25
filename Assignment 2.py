#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2. What are the three different types of Boolean operators?
The three different types of Boolean operators IS "AND", "OR", "NOT". 
These operators are used to manipulate Boolean values and to create more complex logical expressions .

i. AND operator :  The AND operator is represented by the symbol "&&" or word "AND". The "AND" operatore returns "true" if both 
    operands are "true"; otherwise, it returns "false" . 
    for example 
    true AND true = true
    true AND false = false
    false AND false = false
    "A && B," the result is true only if both A and B are true.
    
ii. OR operator :  The OR operator is represented by the symbol "||" or the word "OR." The OR operator returns "true" if at least
    one of the operands is "true"; otherwise , it returns "false". 
    for example :
        true OR true = true
        true OR false = true
        false OR false = false

iii. NOT operator : The NOT operator is represented by the symbol "!" or the word "NOT". The "NOT" operator returns the opposite
    of the operand . If the operand is "true" it returns "false" ,if the operand is "false" it returns "true".
    for example :
        NOT true = false
        NOT false = true
    
These Boolean operators are commonly used in programming and logical operations to evaluate conditions and make decisions based on 
the truth values of expressions.
    
    


# #1. What are the two values of the Boolean data type? How do you write them?
# The two values of the Boolean data type are "true" and "false". In programming ,these values are often represented using literals (the raw data assigned to variables or constants while programming)
# "true" and "false" or using values 0 and 1 ,respectively. in many programming languages, Boolean values are used in conditional statements and logical expressions 
# to control the flow of program execution and to make decision based on the value of particular variable or expression .
# for example
# x = True
# y = false

# In[1]:


a=True
b=False
print(a)
print(b)

 #3 Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
    #values for the operator and what it evaluate
    
 Ans : True and True is True.

       True and False is False.

       False and True is False.

       False and False is False.

       True or True is True.

       True or False is True.

       False or True is True.

       False or False is False.

       not True is False.

       not False is True.
       
     True is 1 and False is 0
     
     Truth Table for AND
      A B output
      0 0 0
      0 1 0
      1 0 0
      1 1 1
      
      Truth Table for OR
      A B output
      0 0 0
      0 1 1
      1 0 1
      1 1 1
      
      Truth Table for NOT
      A output
      0 1
      1 0
      
      
     
        
        

    
    
# Q4. What are the values of the following expressions?

# In[2]:


print((5>4) and (3==5))
print(not(5>4))
print((5>4) or (3==5))
print(not(5>4) or (3==5))
print((True and True) and (True==False))
print((not(False))or(not(True)))


# Q5. What are the six comparison operators?
# 
# Ans . ==, !=, <, >, <=, and >=
# 
# 

# Q6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
#    == is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable.

# In[3]:


# Equal To Operator
if(3==4):
    print("True")
else:
    print("False")
#Assignment operator
c=2 #here we have used assignment operator(=) to assign value of c which is 1
print("c =",c)


#  Q7. Identify the three blocks in this code:

# In[4]:


spam = 0
if spam == 10:
    print('eggs') #Block 1
if spam > 5:
    print('bacon') #Block 2
else:
    print('ham') #Block 3
    print('spam')
    print('spam')


#  Q9. If your programme is stuck in an endless loop, what keys you’ll press?
#  Ans. If my program is stuck in an endless loop, the most common key combination to interrupt the execution and terminate the loop would be:
# Ctrl + C
# 
# 
# 
# 

# Q8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything
# else is stored in spam.

# In[4]:


spam = int(input("Input a no."))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
     


# Q10. How can you tell the difference between break and continue?

# In[6]:


# break
for i in range(10):
   if(i==8):
       break
   print(i)
   
print('Breaked')

#continue
for i in range(10):
   if(i==8):
       continue
   print(i)
 


# Q11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[7]:


for i in range(10):
    print(i)
print("shruti") 
for i in range(0,10):
    print(i)
print("shruti")
for i in range(0,10,1):
    print(i)


# In[ ]:




