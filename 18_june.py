#!/usr/bin/env python
# coding: utf-8

# Q1. What is the role of the 'else' block in a try-except statement? Provide an example scenario where it would be useful.
# 
# Ans. The else block in a try-except statement is an optional block that is executed if no exceptions are raised within the try block. Its role is to specify the code that should be executed when the try block runs successfully without any exceptions.
# 
# 
# 

# In[2]:


class check_mark(Exception):
    "Raised when input marks is less than 80"
    pass


# In[3]:


n = 80
try:
    input_marks = int(input("enter your marks: "))
    if input_marks < n:
        raise check_mark
    else:
        print("you are pass")
except check_mark:
    print("you are fail")
    


# Q2. Can a try-except block be nested inside another try-except block? Explain with an
# example.
# 
# Ans.Yes, a try-except block can be nested inside another try-except
# block in Python. This nesting allows for handling exceptions at 
# different levels of code execution, providing more granular error 
# handling.

# In[4]:


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    try:
        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numbers.")


# Q4. What are some common exceptions that are built-in to Python?
# 
# Ans. TypeError: Raised when an operation or function is performed on an object of inappropriate type.
# 
# ValueError: Raised when a function receives an argument of the correct type but an invalid value.
# 
# ZeroDivisionError: Raised when division or modulo operation is performed with zero as the divisor.
# 
# IndexError: Raised when an index is out of range for a sequence (e.g., list, tuple, string).
# 
# KeyError: Raised when a dictionary key is not found.
# 
# FileNotFoundError: Raised when an attempt is made to open a file that does not exist.

# Q5. What is logging in Python, and why is it important in software development?
# 
# Ans. Logging in Python that allows developers to record and store information about the execution of a program. It involves capturing and storing log messages that provide insights into the program's behavior, errors and other relevant information. Python's logging module provides a flexible logging framework that can be easily integrated into applications.
# 
# 

# Q7. What are log formatters in Python logging, and how can you customise the log message format using formatters?
# 
# Ans.The handlers use logging. Formatter objects to format a log record into a string-based log entry. Note: Formatters do not control the creation of log messages. A formatter works by combining the fields/data in a log record with the user-specified format string.
# 
# In Python's logging module, log formatters are objects that define the structure and content of log messages. They specify the format in which log records are displayed or written to various destinations such as the console, files, or external services.
# 
# The logging.Formatter class is the base class for all log formatters in Python. It allows you to define a format string that determines how log records are formatted. This format string can contain placeholders for various attributes of the log record, such as the log level, timestamp, module name, and the log message itself.

# Q8. How can you set up logging to capture log messages from multiple modules or classes in a Python application?

# In[3]:


import logging
logging.basicConfig(level = logging.DEBUG)
logging.debug("This is debug message")
logging.info("This is my information message")
logging.warning("This is warning message")
logging.error("This is a error message")
logging.critical("This is a CRITICAL message")


# Q9. What is the difference between the logging and print statements in Python? When should you use logging over print 
# statements in a real-world application?
# 
# ans. The logging and print statements in Python serve different purposes and have distinct use cases in real-world applications:
# 
# Purpose:
# 
# Logging: The logging module is designed specifically for generating log messages to provide information about the runtime behavior of an application. It allows you to record events, errors, warnings, and other information systematically.
# Print Statements: The print statement is primarily used for immediate output of values or debugging information during development.
# Output:
# 
# Logging: Log messages can be directed to different handlers, such as console, files, or external services. They can be formatted, filtered, and stored for future analysis. Logging provides structured and configurable output.
# Print Statements: The output of print statements goes to the standard output (console) by default, and it cannot be easily redirected or stored for later analysis.
# Granularity and Levels:
# 
# Logging: The logging module provides multiple levels of granularity, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL. You can selectively enable or disable log messages based on their level. This allows you to control the verbosity of log output and focus on specific levels of interest.
# Print Statements: Print statements provide a single level of output and are typically used for immediate debugging or quick information display without granular control.
# Configurability:
# 
# Logging: The logging module offers extensive configurability. You can define different loggers, handlers, formatters, and filters to customize the log output according to your application's needs. This includes controlling the log level, formatting, output destinations, and more.
# Print Statements: Print statements lack configurability, as they output the provided text as-is without any formatting or customization options.
# Based on these differences, it is recommended to use logging over print statements in real-world applications for the following reasons:
# 
# Flexibility: Logging provides greater flexibility and configurability for managing and controlling log output in different environments, such as development, testing, and production.
# Structured Information: Log messages can include timestamps, log levels, module names, and other contextual information, making it easier to analyze and troubleshoot issues.
# Granularity: By using different log levels, you can filter and focus on specific types of log messages, reducing noise and allowing you to prioritize the importance of different log events.
# Separation of Concerns: Logging allows you to separate the concerns of generating log messages from the actual application logic, enabling better code organization and maintainability.
# Long-term Analysis: Log messages can be stored in files or external services, providing a historical record of application behavior for analysis and debugging purposes.
# However, print statements can still be useful during development for quick and temporary debugging purposes when immediate output is sufficient and configurability is not a concern.
