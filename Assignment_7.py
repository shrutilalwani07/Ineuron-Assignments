#!/usr/bin/env python
# coding: utf-8

# 1.Create two int type variables, apply addition, subtraction, division and multiplications
# and store the results in variables. Then print the data in the following format by calling the
# variables:

# In[1]:


num1 = 10
num2 = 5

# addition
addition_result = num1 + num2

# subtraction
subtraction_result = num1 - num2

# division
division_result = num1 / num2

#  multiplication
multiplication_result = num1 * num2

print("Addition Result: " + str(addition_result))
print("Subtraction Result: " + str(subtraction_result))
print("Division Result: " + str(division_result))
print("Multiplication Result: " + str(multiplication_result))


# 2.What is the difference between the following operators:
# (i) ‘/’ & ‘//’
# (ii) ‘**’ & ‘^’
# 
# (i) The operators '/' and '//' are both used for division in Python, but they behave differently depending on the operands.
# 
# The '/' operator performs regular division and returns a floating-point result. For example, 7 / 2 would yield 3.5, as it calculates the quotient with decimal precision.
# 
# The '//' operator performs floor division or integer division, which rounds down the quotient to the nearest integer. For example, 7 // 2 would yield 3, as it discards the decimal part of the division result and returns the integer part.

# In[2]:


a = 7 / 2    
b = 7 // 2   
print(a)
print(b)


# (ii) The operators '**' and '^' are used for exponentiation or raising a number to a power in Python. However, the '^' operator does not represent exponentiation in Python. Instead, it is the bitwise XOR operator.
# 
# The '**' operator performs exponentiation and calculates the power of a number. For example, 2 ** 3 would yield 8, as it raises 2 to the power of 3.
# 
# The '^' operator, when used between two integers, performs a bitwise XOR operation. It compares the corresponding bits of two numbers and returns a new number with bits set to 1 where the corresponding bits in the operands are different.

# In[3]:


a = 2 ** 3 
b = 2 ^ 3    
print(a)
print(b)


# 3.List the logical operators.
# 
# Ans.In Python, the logical operators are:
# 
# and: The and operator returns True if both operands are True, otherwise it returns False.
# 
# or: The or operator returns True if at least one of the operands is True, otherwise it returns False.
# 
# not: The not operator is a unary operator that returns the opposite boolean value of its operand. If the operand is True, not returns False, and if the operand is False, not returns True.

# In[5]:


a = True
b = False
print(a and b) 
print(a or b)   
print(not a) 


# 4. Explain right shift operator and left shift operator with examples.
# 
# Right Shift Operator (>>):
# The right shift operator shifts the bits of an integer to the right by a specified number of positions. It effectively divides the integer by 2 raised to the power of the specified number. The rightmost bits are discarded, and the leftmost bits are filled with the sign bit (0 for positive numbers and 1 for negative numbers). The syntax for the right shift operator is number >> positions.

# In[6]:


x = 10 
result = x >> 2  

print(result) 


# Left Shift Operator (<<):
# The left shift operator shifts the bits of an integer to the left by a specified number of positions. It effectively multiplies the integer by 2 raised to the power of the specified number. The rightmost bits are filled with zeros, and the leftmost bits are discarded. The syntax for the left shift operator is number << positions.

# In[8]:


x = 10  
result = x << 2  
print(result)


# 5. Create a list containing int type data of length 15. Then write a code to check if 10 is present in the list or not.

# In[9]:


my_list = [5, 3, 8, 12, 6, 7, 10, 15, 20, 25, 18, 30, 1, 9, 4]
if 10 in my_list:
    print("10 is present in the list.")
else:
    print("10 is not present in the list.")


# In[ ]:




