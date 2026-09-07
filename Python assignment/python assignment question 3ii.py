#.(II) Create a class called Book with a constructor (__init__) that initializes:Title,Author,Price and
# Write a method that displays the book details.Instantiate two book objects.

# Part 3.ii: Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

# Instantiate two book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book("1984", "George Orwell", 8.99)

# Display details of the books
print("\nBook 1 details:")
book1.display_details()

print("\nBook 2 details:")
book2.display_details()