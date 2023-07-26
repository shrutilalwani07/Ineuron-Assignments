#!/usr/bin/env python
# coding: utf-8

# Q1. What is the primary goal of Object-Oriented Programming (OOP)?
# 
# Ans. The main purpose of OOP is to combine operative data and functions. It also stops the other functions to access the code except for the one that has been assigned.
#                                    To hold entire data into a single object such that it would be easy to pass this to other methods and objects.

# Q2. What is an object in Python?
# 
# Ans. An Object is an instance of a Class. An object in Python is a self-contained unit that bundles both data (attributes) and the functions (methods) that operate on that data. 

# Q3. What is a class in Python?
# 
# Ans. A class is like a blueprint while an instance is a copy of the class with actual values. A class is a blueprint or a template for creating objects. It defines a set of attributes (variables) and methods (functions) that will be associated with the objects created from the class. 

# Q4. What are attributes and methods in a class?
# 
# Ans. Attributes:
#      Attributes are variables associated with the objects created from a class. Attributes are defined in the class body and are      accessed using the self keyword within the methods of the class.
#      
#    Methods:
#    Methods are functions defined in the class, which operate on the attributes of the class or perform specific actions            associated with the class. 

# Q5. What is the difference between class variables and instance variables in Python?
# 
# Ans. Class variables are useful for storing data that is shared among all instances of a class, such as constants or default          values. Instance variables are used to store data that is unique to each instance of a class, such as object properties.
#       Class variables are variables that are shared among all instances (objects) of a class. They are defined within the class body but outside any methods using the class keyword. 
#      
#    Instance variables are variables that are specific to each instance (object) of a class. They are defined within the class's methods, usually within the __init__() method, using the self keyword. 

# Q6. What is the purpose of the self parameter in Python class methods?
# 
# Ans. The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. The self parameter allows methods to access and manipulate the attributes (instance variables) of the specific object it is called on. When you call a method on an instance of a class, Python automatically passes the instance as the first argument to the method, and you need to include the self parameter in the method definition to capture and work with that instance.

# Q7. For a library management system, you have to design the "Book" class with OOP
# principles in mind. The “Book” class will have following attributes:
# a. title: Represents the title of the book.
# b. author: Represents the author(s) of the book.
# c. isbn: Represents the ISBN (International Standard Book Number) of the book.
# d. publication_year: Represents the year of publication of the book.
# e. available_copies: Represents the number of copies available for checkout.
# The class will also include the following methods:
# a. check_out(self): Decrements the available copies by one if there are copies
# available for checkout.
# b. return_book(self): Increments the available copies by one when a book is
# returned.
# c. display_book_info(self): Displays the information about the book, including its
# attributes and the number of available copies.

# In[20]:


class Book:
    def __init__(self,title,author,isbn,publication_year,available_copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.publication_year=publication_year
        self.available_copies=available_copies
        
    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"{self.title} checked out successfully. {self.available_copies} copy(s) available.")
        else:
            print(f"Sorry, {self.title} is currently out of stock.")
            
    def return_book(self):
        self.available_copies +=1
        print(f"Thanks for return {self.title}.{self.available_copies} copy(s) available." )
    
    def display_book_info(self):
        print(f"Year of Publication : {self.publication_year}")
        print(f"title :{self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        


# In[21]:


book1= Book("the power of thinking","eintein","638903464538303-89765",2002,2)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061122416", 1960, 3)

book1.display_book_info()
book1.check_out()
book1.check_out()
book1.return_book()

book2.display_book_info()
book2.check_out()
book2.check_out()



# Q8. For a ticket booking system, you have to design the "Ticket" class with OOP
# principles in mind. The “Ticket” class should have the following attributes:
# a. ticket_id: Represents the unique identifier for the ticket.
# b. event_name: Represents the name of the event.
# c. event_date: Represents the date of the event.
# d. venue: Represents the venue of the event.
# e. seat_number: Represents the seat number associated with the ticket.
# f. price: Represents the price of the ticket.
# g. is_reserved: Represents the reservation status of the ticket.
# The class also includes the following methods:
# a. reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
# b. cancel_reservation(self): Cancels the reservation of the ticket if it is already
# reserved.
# c. display_ticket_info(self): Displays the information about the ticket, including its
# attributes and reservation status.

# In[12]:


class Ticket:
    def __init__(self, ticket_id, event_name, event_date, venue, seat_number, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.seat_number = seat_number
        self.price = price
        self.is_reserved = False

    def reserve_ticket(self):
        if not self.is_reserved:
            self.is_reserved = True
            print(f"Ticket {self.ticket_id} is now reserved.")
        else:
            print(f"Ticket {self.ticket_id} is already reserved.")

    def cancel_reservation(self):
        if self.is_reserved:
            self.is_reserved = False
            print(f"Reservation for Ticket {self.ticket_id} has been canceled.")
        else:
            print(f"Ticket {self.ticket_id} is not reserved, so there's nothing to cancel.")

    def display_ticket_info(self):
        print("Ticket Information:")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Venue: {self.venue}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: {self.price}")
        print(f"Reservation Status: {'Reserved' if self.is_reserved else 'Not Reserved'}")





# In[13]:


ticket1 = Ticket(101, "Consistency", "2023-06-24", "Cenetred", "S-24", 24)
ticket1.display_ticket_info()
ticket1.reserve_ticket()
ticket1.reserve_ticket()
ticket1.cancel_reservation()
ticket1.display_ticket_info()


# Q9. You are creating a shopping cart for an e-commerce website. Using OOP to model
# the "ShoppingCart" functionality the class should contain following attributes and
# methods:
# a. items: Represents the list of items in the shopping cart.
# The class also includes the following methods:
# a. add_item(self, item): Adds an item to the shopping cart by appending it to the
# list of items.
# b. remove_item(self, item): Removes an item from the shopping cart if it exists in
# the list.
# c. view_cart(self): Displays the items currently present in the shopping cart.
# d. clear_cart(self): Clears all items from the shopping cart by reassigning an
# empty list to the items attribute
# 
# 

# In[40]:


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to the shopping cart.")
        
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} is removed from shopping cart")
        else:
            print(f"{item} not find in the cart")
            
    def view_cart(self):
        if not self.items:
            print("cart is empty.")
        else:
            print("Items in your shopping cart:")
            for item in self.items:
                print(f"- {item}")
                
    def clear_cart(self):
        self.items.clear()
        print("Shopping cart cleared.")


# In[42]:


#add
cart = ShoppingCart()
cart.add_item("Shampoo")
cart.add_item("Conditioner")
cart.add_item("Oil")
#remove
cart.remove_item("Conditioner")
#view
cart.view_cart()
#clear
cart.clear_cart()
cart.view_cart()


# Q10. Imagine a school management system. You have to design the "Student" class using
# OOP concepts.The “Student” class has the following attributes:
# a. name: Represents the name of the student.
# b. age: Represents the age of the student.
# c. grade: Represents the grade or class of the student.
# d. student_id: Represents the unique identifier for the student.
# e. attendance: Represents the attendance record of the student.
# The class should also include the following methods:
# a. update_attendance(self, date, status): Updates the attendance record of the
# student for a given date with the provided status (e.g., present or absent).
# b. get_attendance(self): Returns the attendance record of the student.
# c. get_average_attendance(self): Calculates and returns the average
# attendance percentage of the student based on their attendance record.

# In[53]:


class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.attendance = {}  # Using a dictionary to store the attendance record with dates as keys and statuses as values

    def update_attendance(self, date, status):
        self.attendance[date] = status

    def get_attendance(self):
        return self.attendance

    def get_average_attendance(self):
        if not self.attendance:
            return 0.0

        total_days = len(self.attendance)
        present_days = sum(status == "present" for status in self.attendance.values())
        attendance_percentage = (present_days / total_days) * 100
        return round(attendance_percentage, 2)




# In[56]:


students= Student("Riya",18,"12-Grade","0235675")
students.update_attendance("20-07-23","Present")
students.update_attendance("21-07-23","Absent")

attendance_record = students.get_attendance()
print(attendance_record)

average_attendance = students.get_average_attendance()
print(f"Average attendance percentage: {average_attendance}%")


# In[ ]:




