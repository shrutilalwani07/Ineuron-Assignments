#!/usr/bin/env python
# coding: utf-8

# Q1.  In Python, what is the difference between a built-in function and a user-defined function? Provide an
# example of each.
# Ans. Built-in functions:
# Built-in functions are functions that are already provided by the Python programming language.
# They are readily available for use without requiring any additional coding or importing external modules.
# These functions are implemented in the Python interpreter and cover a wide range of operations, 
# such as mathematical calculations, string manipulations, file handling, etc.
# Example of a built-in function:
# 

# In[1]:


name = "Shruti lalwani"
length = len(name)
print(length) 


# User-defined functions:
# User-defined functions are functions that are created by the user to perform specific tasks.
# They allow you to encapsulate a sequence of code into a reusable block, enhancing code organization,
# readability, and maintainability. User-defined functions are defined using the def keyword, followed 
# by a function name, parameter list (if any), and a block of code to be executed when the function is called.

# In[2]:


def multiply_area(l,w):
    area = l * w
    return area
reactangle_area = multiply_area(4,5)
print(reactangle_area)


# Q2. How can you pass arguments to a function in Python? Explain the difference between positional
# arguments and keyword arguments.
# 
# Ans. Positional Arguments: During a function call, values passed through arguments should be in the order
#      of parameters in the function definition.
#      Keyword Arguments: Keyword arguments (or named arguments) are values that, when passed into a function,
#      are identifiable by specific parameter names.

# In[11]:


#positional argument
def college(name, branch):
    print(f"Hello, {name}! You are from  {branch} 4th year student.")

college("Shruti", "artificial inteligence and data science")


# In[12]:


#keyword argument
def student(name, age):
    print(f"Hello, {name}! You are {age} years old.")

student(age=20, name="siya")


# The main diffreence of positional argument and keyword argument is
# Positional arguments must be included in the correct order. Keyword arguments are included with a keyword and equals sign.
# 
# - Positional Argument : 
#   Positional arguments are passed to a function based on their position or order.
#   The values for positional arguments are provided in the same order as the parameters are defined in the function signature.
#   The number of positional arguments passed must match the number of parameters in the function signature.
#   
# - Keyword Argument :
#   Keyword arguments are passed to a function using the parameter names and corresponding values
#   The order of keyword arguments does not matter.
#   Keyword arguments allow you to explicitly specify which values are assigned to which parameters.
# 

# Q3. What is the purpose of the return statement in a function? Can a function have multiple return
#     statements? Explain with an example
#     
# Ans. The purpose of the return statement in a function is to specify the value or values that the 
#      function should output when it is called. It allows the function to pass back data to the caller.
#     
#     A function can have multiple return statements, but only one of them will be executed during the function's execution. When a return statement is encountered, the function immediately exits, and the value specified after the return keyword is returned as the result of the function.
# 
# 

# In[2]:


# for example
def find_maximum(numbers):
    if len(numbers) == 0:
        return None  # If the list is empty, return None

    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum  # Return the maximum value


numbers_list = [4, 7, 2, 10, 5]
result = find_maximum(numbers_list)
print(result)  


# Q4. What are lambda functions in Python? How are they different from regular functions? Provide an
# example where a lambda function can be useful
# 
# Ans.Lambda functions, also known as anonymous functions, are a concise way to create small, one-line functions in Python. Unlike regular functions defined using the def keyword, lambda functions are defined using the lambda keyword.
# 
# The main differences between lambda functions and regular functions are:
# 
# Syntax: Lambda functions have a compact syntax compared to regular functions. They are defined using the lambda keyword followed by the arguments and a colon, and the expression that is returned.
# 
# Namelessness: Lambda functions are anonymous; they don't have a specific name. They are primarily used for immediate, short-lived operations.
# 
# Limited Functionality: Lambda functions are restricted to a single expression. They cannot contain multiple lines of code, statements, or complex control flow. Regular functions, on the other hand, can consist of multiple statements and have more flexibility.

# In[3]:


# for example
products = [{'name' : 'Phone', 'price' : 10000},
            {'name' : 'Printer', 'price' : 20000},
            {'name' : 'Mouse', 'price' : 5000},
           {'name' : 'Laptop', 'price' : 40000},]
sorted_products = sorted(products, key  = lambda x:  x['price'],
                        reverse = True)

for products in sorted_products:
    print(products)


# Q5. How does the concept of "scope" apply to functions in Python? Explain the difference between local
# scope and global scope.
# 
# Ans. In Python, "scope" refers to the region or context in which a variable, name, or object is defined and can be accessed. The concept of scope applies to functions in Python, and it determines the visibility and accessibility of variables within a function.
# 
# Local Scope:
# Local scope refers to the variables that are defined within a function. These variables are only accessible from within the function and are not visible outside of it.
# Local variables have a limited lifespan, as they are created when the function is called and destroyed when the function execution is complete.
# Local variables take precedence over variables with the same name in higher-level scopes.
# 
# Global Scope:
# Global scope refers to the variables that are defined outside of any function, at the top level of a module. These variables can be accessed from anywhere within the module.
# Global variables have a longer lifespan compared to local variables, as they are created when the module is imported and persist until the program terminates.
# Global variables can be accessed within functions, but if a variable with the same name is defined locally within a function, it will shadow the global variable within that function.
# 

# Q6. How can you use the "return" statement in a Python function to return multiple values?
# 
# Ans. In Python, the return statement in a function is used to specify    the value that the function should return when it is called. By default, a return statement can only return a single value. However, you can return multiple values from a function by using different techniques.
# 
# Returning Multiple Values as a Tuple:
# You can return multiple values as a tuple by separating them with commas. When the function is called, the values will be bundled together into a tuple and returned.
# 

# In[5]:


# for example
def get_values():
    x = 150
    y = 250
    z = 300
    return x, y, z

result = get_values()
print(result)  


# Q7. What is the difference between the "pass by value" and "pass by reference" concepts when it
# comes to function arguments in Python?
# 
# Ans. In Python, the concepts of "pass by value" and "pass by reference" are not applicable in the same way as in some other programming languages. The behavior in Python can be described as "pass by object reference" or "pass by assignment."
# 
# In Python, when you pass an argument to a function, you are actually passing a reference to the object rather than the object itself. The behavior of the function depends on whether the object being passed is mutable or immutable.
# 
# Immutable Objects (Pass by Object Reference):
# Immutable objects, such as numbers, strings, and tuples, cannot be modified after they are created. When an immutable object is passed as an argument to a function, a copy of the reference to the object is made. However, the original object itself cannot be modified within the function.

# In[1]:


def modify_value(num):
    num += 10 
    print("Inside the function:", num)

value = 5
modify_value(value)
print("Outside the function:", value)


# Mutable Objects (Pass by Object Reference):
# Mutable objects, such as lists and dictionaries, 
# can be modified after they are created. When a mutable object is 
# passed as an argument to a function, a copy of the reference to the
# object is made. The function can modify the object in-place,
# affecting the original object itself.

# In[2]:


def modify_list(my_list):
    my_list.append(4)  
    print("Inside the function:", my_list)

numbers = [1, 2, 3]
modify_list(numbers)
print("Outside the function:", numbers)


# In[5]:


# Q8. Create a function that can intake integer or decimal value and do following operations:
# a. Logarithmic function (log x)
# b. Exponential function (exp(x))
# c. Power function with base 2 (2x)
# d. Square root

import math
def perform_operations(x):
    result = {}
    # Logarithmic function (log x)
    result['log'] = math.log(x)

    # Exponential function (exp(x))
    result['exp'] = math.exp(x)

    # Power function with base 2 (2^x)
    result['power'] = math.pow(2, x)

    # Square root
    result['sqrt'] = math.sqrt(x)

    return result

# Test the function
value = 2.5
operations_result = perform_operations(value)

print(f"Logarithmic function (log {value}): {operations_result['log']}")
print(f"Exponential function (exp({value})): {operations_result['exp']}")
print(f"Power function with base 2 (2^{value}): {operations_result['power']}")
print(f"Square root of {value}: {operations_result['sqrt']}")



# Q9. Create a function that takes a full name as an argument and returns first name and last name

# In[6]:


def introduction(firstname, lastname): 
    print(firstname)
    print(lastname)
    


# In[7]:


introduction("Shruti", "lalwani")


# In[ ]:




