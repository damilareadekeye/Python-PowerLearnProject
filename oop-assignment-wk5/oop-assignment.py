# OOP Assignment - Week 5

# Assignment 1: Design Your Own Class
# Create a class representing a Book.

class Book:
    """
    Represents a book with a title, author, and publication year.
    """
    def __init__(self, title, author, year):
        """
        Initializes a Book object with a title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        """
        Returns a string describing the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}."

# Add an inheritance layer
class FictionBook(Book):
    """
    Represents a fiction book, which is a type of Book, with an added genre.
    """
    def __init__(self, title, author, year, genre):
        """
        Initializes a FictionBook object.
        """
        super().__init__(title, author, year)
        self.genre = genre

    def get_description(self):
        """
        Returns a string describing the fiction book, including its genre.
        (This demonstrates polymorphism as it overrides the parent method).
        """
        return f"{self.title} by {self.author}, a {self.genre} novel published in {self.year}."

# Activity 2: Polymorphism Challenge
# Create classes for different vehicles with a 'move' method.

class Vehicle:
    """
    Base class for all vehicles.
    """
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    """
    Represents a car that drives.
    """
    def move(self):
        return "Driving..."

class Plane(Vehicle):
    """
    Represents a plane that flies.
    """
    def move(self):
        return "Flying..."

class Boat(Vehicle):
    """
    Represents a boat that sails.
    """
    def move(self):
        return "Sailing..."


# --- Demonstration ---

# Assignment 1 Demo
print("--- Assignment 1: Book Class ---")
# Create a standard book object
my_book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(my_book.get_description())

# Create a fiction book object
my_fiction_book = FictionBook("Dune", "Frank Herbert", 1965, "Science Fiction")
print(my_fiction_book.get_description())
print("\n" + "-"*20 + "\n")


# Activity 2 Demo
print("--- Activity 2: Polymorphism Challenge ---")
# Create instances of different vehicles
car = Car()
plane = Plane()
boat = Boat()

# Call the move method on each vehicle
print(f"Car: {car.move()}")
print(f"Plane: {plane.move()}")
print(f"Boat: {boat.move()}")
