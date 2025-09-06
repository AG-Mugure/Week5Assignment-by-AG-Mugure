# Base class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.__price = price   # encapsulated (private attribute)

    # Encapsulation: getter and setter for price
    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    def read(self):
        return f"Reading '{self.title}' by {self.author}..."

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, Price: ${self.__price}"


# Derived class for EBooks
class EBook(Book):
    def __init__(self, title, author, pages, price, file_size):
        super().__init__(title, author, pages, price)
        self.file_size = file_size  # in MB

    # Polymorphism: redefine read() method
    def read(self):
        return f"Reading '{self.title}' by {self.author} on an e-reader. (File size: {self.file_size}MB)"


# Derived class for AudioBooks
class AudioBook(Book):
    def __init__(self, title, author, pages, price, duration):
        super().__init__(title, author, pages, price)
        self.duration = duration  # in hours

    # Polymorphism: redefine read() method
    def read(self):
        return f"Listening to '{self.title}' by {self.author}. Duration: {self.duration} hours."


# Example usage
book1 = Book("Pride and Prejudice", "Jane Austen", 432, 15.99)
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 9.99, 5)
audiobook1 = AudioBook("Becoming", "Michelle Obama", 448, 19.99, 19)

# Test them out
print(book1)
print(book1.read())
print(ebook1)
print(ebook1.read())   # Polymorphism in action
print(audiobook1)
print(audiobook1.read())

# Encapsulation test
print("Old Price:", book1.get_price())
book1.set_price(12.49)
print("New Price:", book1.get_price())
