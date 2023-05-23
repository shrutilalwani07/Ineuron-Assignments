#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1 In the below elements which of them are values or an expression? eg:- values can be
#integer or string and expressions will be mathematical operators.
#*
#&#39;hello&#39;
#-87.8
#-
#/
#+ 

elements = ['*', 'hello', -87.8, '-', '/', '+']

for element in elements:
    if isinstance(element, str) or isinstance(element, int) or isinstance(element, float):
        print(f'{element} is a value.')
    else:
        print(f'{element} is an expression.')

custom_input = input("Enter a value or expression: ")
print(f'You entered: {custom_input}')


# In[ ]:


# Q2 What is the difference betweent string and variable?
String: A string is a sequence of characters enclosed within single quotes ('') or double quotes (" "). It is a data type used to represent textual data. Strings are immutable, meaning they cannot be changed once created. You can perform various operations on strings, such as concatenation, slicing, and formatting. for example 
my_string = "Hello I am shruti!"

Variable : A Python variable is a symbolic name that is a reference or pointer to an object.Variables are containers for storing data values. Variables can hold different types of values, including strings, numbers, lists, etc. 
A variable is a named storage location in a program that can hold a value. It acts as a container for storing different types of data, including strings, numbers, and other data types.
for example x = 5


# In[ ]:


# Q3 Describe three different data types
List (list): Lists are ordered collections of items, enclosed within square brackets ([]). They can contain elements of different data types, including integers, strings, or even other lists. 
Lists are mutable (changeable), allowing you to modify, add, or remove elements. They are used to store and organize multiple items in a single variable
for example 
fruits = ["banana", "grapes", "mango"]
print(fruits)

Tuple (tuple) : Tuple is immutanle (unchangeable) . A tuple is defined using parentheses () and consists of comma-separated values.
for example : 
fruits = ("banana", "grapes", "mango") # 0 to 2
print(fruits) 

Dictionary (dict) : A dictionary is defined using curly braces {} and consists of comma-separated key-value pairs.
It is used to store a collection of key-value pairs. It is an unordered and mutable (changeable) data type.
for example :
my_dict = {"name" : "Tom", "subject" : "english", "marks" :" 40"}
print(my_dict)
 


# In[ ]:


# Q4 What is an expression made up of? What do all expressions do?
Expressions can be used in various contexts, such as assignments, conditionals, loops, and function calls. They are evaluated by the Python interpreter to produce a result. The result can be used further in the program, assigned to a variable, or used in other expressions.
an expression is a combination of values, variables, operators, and function calls that produces a result. It can be as simple as a single value or variable, or it can be a complex combination of multiple elements. Expressions are used to perform computations and evaluate to a value.

Values: These are literal values such as numbers (integers or floating-point numbers) or strings. For example 9, 6.14, or 'Welcome'.

Variables: These are named references to values stored in memory. Variables hold data that can be used within expressions. For example S, Class, or sum.

Operators: These are symbols or special keywords used to perform operations on values or variables. Python supports various operators, including arithmetic operators (+, -, *, /), comparison operators (<, >, ==, !=), logical operators (and, or, not), assignment operators (=, +=, -=, etc.), and more.

Function Calls: These are invocations of functions that can take arguments and return a value. Functions can be built-in functions provided by Python or user-defined functions. For example, len('Hello') or math.sqrt(81).


# In[ ]:


# Q5 This assignment statements, like spam = 10.What is the difference between an expression and a statement?
An assignment statement, such as spam = 10, is used to assign a value to a variable. It associates a variable name with a value, allowing you to store and manipulate data within your program. Here is a breakdown of the components and behavior of an assignment statement:
1. Variable: In this example, 'spam' is a variable name. It can be any valid identifier that follows Python naming rules, such as starting with a letter or underscore, and consisting of letters, digits, and underscores.
2. Assignment Operator: The assignment operator ('=') is used to assign a value to the variable. It associates the variable on the left side with the value on the right side.
3. Value: The value assigned to the variable is '10' in this case. It can be a literal value (e.g., numbers, strings) or the result of an expression.
4. Evaluation: When the assignment statement is executed, the value on the right side of the assignment operator is evaluated. In this case, 10 is a literal value, so its evaluation is straightforward.
5. Storage: After the value is evaluated, it is stored in the variable on the left side of the assignment operator. In this example, the value 10 is stored in the variable spam. From this point forward, you can refer to the variable spam to access the stored value.
    
Expression: An expression is a combination of values, variables, operators, and function calls that can be evaluated to produce a value. 
It computes or calculates a result. 
Examples of expressions include 7 + 9, 'welcome',   name, or len(my_list). 
Expressions can be used within statements, as part of larger expressions, or they can stand alone and produce a value.

Statement: A statement is a line of code that performs an action or has some effect.
Statements are typically used to control the flow of a program, define behavior, or execute specific tasks.
Examples of statements include assignment statements (spam = 10), conditional statements (if, else, elif), loops (for, while), function definitions etc. 
Statements do not produce a value like expressions do.

    


# In[ ]:


# Q9 What three functions can be used to get the integer, floating-point number, or string version of a value?
The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.

int(): The int() function can be used to convert a value to an integer.
It takes a single argument and returns an integer representation of that value if possible. 
If the value cannot be converted to an integer, a ValueError is raised. For example:
x = int("30")  # Converts the string "10" to an integer 10

float(): The float() function converts a value to a floating-point number. 
It takes a single argument and returns the floating-point representation of the value if possible. 
If the value cannot be converted to a float, a ValueError is raised. For example:
y = float("6.23")  # Converts the string "3.14" to a float 3.14

str(): The str() function is used to convert a value to a string. 
It takes a single argument and returns a string representation of the value. 
The argument can be of any data type, and str() will convert it to a string. For example
z = str(89)  # Converts the integer 42 to a string "42"



    


# In[7]:


# Q6 After running the following code, what does the variable bacon contain?
#bacon = 22
#bacon + 1 
bacon = 22
bacon  = bacon + 1
print(bacon)



# In[ ]:


# Q8 Why is eggs a valid variable name while 100 is invalid?
1. Variable names must start with a letter (a-z, A-Z) or an underscore (_). They cannot start with a number.
2. After the first character, variable names can contain letters, numbers, and underscores.
3. Variable names are case-sensitive. For example, myVariable and myvariable are considered different variables.

Based on these rules, eggs is a valid variable name because it starts with a letter and contains only letters.
It follows the rules for naming variables in Python.

On the other hand, 100 is an invalid variable name because it starts with a number. 
Variable names cannot start with a number according to the naming rules. 
If you want to include numbers in a variable name, they must come after the first character. 
For example, eggs100 would be a valid variable name in Python.
variable start with alphabets then will add numeric value 
for example 
shruti 100


# In[ ]:




