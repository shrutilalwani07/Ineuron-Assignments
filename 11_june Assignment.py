#!/usr/bin/env python
# coding: utf-8

# Q1. What is a lambda function in Python, and how does it differ from a regular function?
# 
# Ans. Ans.Lambda functions, also known as anonymous functions, are a concise way to create small, one-line functions in Python. Unlike regular functions defined using the def keyword, lambda functions are defined using the lambda keyword.
# 
# The main differences between lambda functions and regular functions are:
#  
# Syntax: Lambda functions have a compact syntax compared to regular functions. They are defined using the lambda keyword followed by the arguments and a colon, and the expression that is returned.
# 
# Namelessness: Lambda functions are anonymous; they don't have a specific name. They are primarily used for immediate, short-lived operations. 
# 
#  Limited Functionality: Lambda functions are restricted to a single expression. They cannot contain multiple lines of code, statements, or complex control flow. Regular functions, on the other hand, can consist of multiple statements and have more flexibility.

# In[1]:


# for example
products = [{'name' : 'Phone', 'price' : 10000},
            {'name' : 'Printer', 'price' : 20000},
            {'name' : 'Mouse', 'price' : 5000},
           {'name' : 'Laptop', 'price' : 40000},]
sorted_products = sorted(products, key  = lambda x:  x['price'],
                        reverse = True)

for products in sorted_products:
    print(products)


# Q2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use them?
# 
# Ans. Yes, a lambda function in Python can have multiple arguments.

# In[8]:


# for example 
multiply = lambda x, y: x * y

result = multiply(5, 3)
print(result)  

print("-----------------------")

add_three_numbers = lambda x, y, z: x + y + z

result = add_three_numbers(1, 2, 3)
print(result) 


# Q3. How are lambda functions typically used in Python? Provide an example use case.
# 
# Ans. Lambda functions in Python are typically used in situations where you need a small, anonymous function without the need for a formal function definition. They are particularly useful in functional programming and when you need to pass a function as an argument to another function

# In[13]:


numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

print("------------------------------")
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) 


# Q4. What are the advantages and limitations of lambda functions compared to regular functions in
# Python?
# 
# Ans. Advantages of Lambda Functions :
# 
# 1. Conciseness: Lambda functions allow you to define small, anonymous functions in a compact and readable manner. They can be defined in a single line, making the code more concise and easier to understand.
# 
# 2. Immediate Use: Lambda functions are often used in situations where a function is needed as an argument to another function, such as in functional programming paradigms. They can be defined on-the-fly at the point of use, eliminating the need for a separate function declaration.
# 
# 3. Function Expressions: Lambda functions are expressions rather than statements. This means they can be used in places where regular functions cannot be used, such as inside list comprehensions or as part of other expressions.
# 
# Limitations of Lambda functions 
# 
# Limited functionality : Lambda functions are designed for simple and concise functions. The are best suited for short , one-line expressions. 
# 
# Debugging and Testing: Lambda functions lack a named identifier, which can make it more challenging to debug or test them in isolation. 

# Q5. Are lambda functions in Python able to access variables defined outside of their own scope? Explain with an example.
# 
# Ans. Yes, lambda functions in Python can access variables defined outside of their own scope. They can access variables from the enclosing scope, including global variables and variables defined in the surrounding function.

# In[15]:


# Q6. Write a lambda function to calculate the square of a given number.

square = lambda x: x**2

num = 6
result = square(num)
print(result) 


# In[17]:


# Q7. Create a lambda function to find the maximum value in a list of integers.

numbers = [10,28,34,99,55,8]

max_value = lambda x: max(x)

result = max_value(numbers)
print(result)  


# In[20]:


# Q8. Implement a lambda function to filter out all the even numbers from a list of integers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]


# In[2]:


# Q9. Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.

strings = ["apple", "banana", "eldercherry", "cherry"]
sorted_strings = sorted(strings, key=lambda x: x)
print(sorted_strings)


# Q10. Create a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists.
# 

# In[4]:


list1 = [1, 2, 3, 8, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = lambda x, y: [element for element in x if element in y]
result = common_elements(list1, list2)
print(result)


# Q13. Create a recursive function to find the sum of all the elements in a given list

# In[5]:


def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])
numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print(f"The sum of the list {numbers} is: {result}")


# In[ ]:




