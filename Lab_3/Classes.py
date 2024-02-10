# task 1
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

# task 2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

# Example usage:
shape = Shape()
print("Area of shape:", shape.area())

square = Square(5)
print("Area of square:", square.area())

# task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
rectangle = Rectangle(4, 6)
print("Area of rectangle:", rectangle.area())

# task 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

# Example usage:
point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

distance = point1.dist(point2)
print("Distance between the points:", distance)

point1.move(3, 5)
point1.show()

# task 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal of ${amount} accepted. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

# Example usage:
account = Account("John Doe", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # Should print "Insufficient funds."
account.deposit(-100)   # Should print "Invalid deposit amount."

print("Current balance:", account.balance)
