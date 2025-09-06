# 📚 Book Class with Inheritance, Polymorphism & Encapsulation

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python using a simple but powerful example: a `Book` class and its derived classes `EBook` and `AudioBook`.

---

##  Features

- **Encapsulation**:  
  The `price` attribute is private (`__price`) and can only be accessed/modified through getters and setters (`get_price()` and `set_price()`).

- **Inheritance**:  
  - `EBook` inherits from `Book` and adds a `file_size` attribute.  
  - `AudioBook` inherits from `Book` and adds a `duration` attribute.  

- **Polymorphism**:  
  The `read()` method is overridden in child classes:  
  - `Book` → *Reading the physical book.*  
  - `EBook` → *Reading on an e-reader with file size info.*  
  - `AudioBook` → *Listening with duration info.*  

- **Constructors**:  
  Each object is initialized with its own attributes (title, author, pages, price, etc.).

---

## Project Structure

