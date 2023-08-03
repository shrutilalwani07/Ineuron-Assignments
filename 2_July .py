#!/usr/bin/env python
# coding: utf-8

# Q1. Explain what inheritance is in object-oriented programming and why it is used.
# 
# Ans. Inheritance is a fundamental concept that allows a class to inherit the properties and behaviors (attributes and methods) of another class. 
# Inheritance is used to create a hierarchy of classes, where the child class inherits the characteristics of the parent class, allowing it to reuse and extend the functionality provided by the parent class. 

# Q2. Discuss the concept of single inheritance and multiple inheritance, highlighting their
# differences and advantages.
# 
# Ans. Single inheritance is one in which the derived class inherits the single base class.
#      Multiple inheritance is one in which the derived class acquires two or more base classes. 
#      
#    In single inheritance, the derived class uses the features of the single base class. 
#    While in multiple inheritance, the derived class uses the joint features of the inherited base classes.

# Q3. Explain the terms "base class" and "derived class" in the context of inheritance
# 
# Ans. The new class created is called “derived class” or “child class” and the existing class is known as the “base class” or “parent class”.The class that inherits those members is called the derived class.

# Q4. What is the significance of the "protected" access modifier in inheritance? How does
# it differ from "private" and "public" modifiers?
# 
# Ans. The protected access modifier uses the inheritance level of the entity to set its accessibility to the outside world. This means that we can use the protected access modifier for an entity that we want to be visible in all the classes inheriting its defining class. 
# 
# The difference between public and protected is that public can be accessed from outside class but protected cannot be accessed from outside class

# Q5. What is the purpose of the "super" keyword in inheritance? Provide an example.
# 
# Ans. The super keyword refers to superclass (parent) objects. It is used to call superclass methods, and to access the superclass constructor. The most common use of the super keyword is to eliminate the confusion between superclasses and subclasses that have methods with the same name.
# 

# In[7]:


class Animal:
    def make_sound(self):
        print("Dog is barking")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Woof! Woof!")


# In[8]:


dog_instance = Dog()
dog_instance.make_sound()


# Q6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
# Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
# attribute called "fuel_type". Implement appropriate methods in both classes.

# In[1]:


class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def display_info(self):
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
        
    
        


# In[4]:


class Car(Vehicle):
    def __init__(self,make,model,year,fuel_type):
        super().__init__(make,model,year)
        self.fuel_type=fuel_type
        
    def display_info(self):
        super().display_info()
        print(f"Fuel type :{self.fuel_type}")


# In[5]:


car1=Car("Tata Nexon","coroolo","2023","Diesel")
car1.display_info()


# Q7. Create a base class called "Employee" with attributes like "name" and "salary."
# Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
# attribute called "department" for the "Manager" class and "programming_language"
# for the "Developer" class

# In[17]:


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_info(self):
        print(f"Name :{self.name}")
        print(f"Salary: {self.salary}")
        


# In[24]:


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")


# In[27]:


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Programming Language: {self.programming_language}")


# In[29]:


manager = Manager("Siya", 700000, "HR")
developer = Developer("Arohi", 60000, "Reactjs")


# In[31]:


manager.display_info()
print("-----------")
developer1.display_info()


# Q8. Design a base class called "Shape" with attributes like "colour" and "border_width."
# Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
# specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
# the "Circle" class.
# 

# In[52]:


class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width


# In[53]:


class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width
        
    def display_info(self):
        print(f"Shape: Rectangle")
        print(f"Colour: {self.colour}")
        print(f"Border Width: {self.border_width}")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")


# In[54]:


class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius

    def display_info(self):
        print(f"Shape: Circle")
        print(f"Colour: {self.colour}")
        print(f"Border Width: {self.border_width}")
        print(f"Radius: {self.radius}")


# In[55]:


rectangle=  Rectangle("Pink",2,10,8)
circle = Circle("Blue", 1, 7)

rectangle.display_info()
print("-----------")
circle.display_info()


# 9. Create a base class called "Device" with attributes like "brand" and "model." Derive
# two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
# "screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.
# 

# In[70]:


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# In[71]:


class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Screen Size: {self.screen_size}")


# In[72]:


class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Capacity: {self.battery_capacity}")


# In[73]:


phone1 = Phone("Apple", "iPhone 13", "6.1 inches")
tablet1 = Tablet("Samsung", "Galaxy Tab S7", "8000 mAh")

phone1.display_info()
print("-----------")
tablet1.display_info()


# 10. Create a base class called "BankAccount" with attributes like "account_number" and
# "balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
# "BankAccount." Add specific methods like "calculate_interest" for the
# "SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.

# In[87]:


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


# In[88]:


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self, interest_rate):
        interest = self.balance * (interest_rate / 100)
        self.balance += interest

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")



# In[89]:


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deduct_fees(self, fee):
        self.balance -= fee

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")



# In[91]:


savings_account = SavingsAccount("SHRU27", 5000)
checking_account = CheckingAccount("CHK5678", 3000)

savings_account.calculate_interest(2.5)
checking_account.deduct_fees(50)

savings_account.display_info()
print("-----------")
checking_account.display_info()


# In[ ]:




