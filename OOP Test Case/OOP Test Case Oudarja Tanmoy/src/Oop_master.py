# code-1
# Class and object structure
class Employee:
    def __init__(self, base_salary, overtime, rate):
        # Properties
        self.base_salary = base_salary
        self.overtime = overtime
        self.rate = rate
    # Method
    def get_wage(self):
        return self.base_salary + (self.overtime * self.rate)


# Object
emp1 = Employee(base_salary=30000, overtime=10, rate=20)

# Method call
print(emp1.get_wage())


# code-2
# Types of method in python
class Example:
    count = 0  # Class attribute

    def __init__(self, value):
        self.value = value  # 'self' accesses instance attribute 'value'

    def instance_method(self):
        # Can access both instance and class data
        return f"Value: {self.value}, Count: {Example.count}"

    @classmethod
    def class_method(cls): #Use 'clas' to access class attribute 'count'
        # Accesses or modifies class-level data
        cls.count += 1
        return f"Count updated to: {cls.count}" # Called from the class itself

    @staticmethod
    def static_method(x, y):
        # Does not access class or instance data
        return x + y

ex = Example(10) # Create an instance
print(ex.instance_method()) # Call on an instance
print(Example.class_method())
print(Example.static_method(3, 4)) # Call without creating an instance


# code-3
# Use of __init__ Method in Python
class Student:
    def __init__(self, name, roll):
        self.name = name       # Instance variable
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Creating object
s1 = Student("Alice", 101)
s1.display()  # Output: Name: Alice, Roll: 101


# code-4

# Abstraction:

# An abstract class is a class that cannot be instantiated and is
# meant to be inherited by other classes. It serves as a blueprint for child classes.

# An abstract method is a method that has no implementation in the parent class and must
# be implemented in the child class.
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract *Model*
    @abstractmethod
    def area(self):  # Abstract *Method*
        pass

class Circle(Shape):  # Subclass *Model*
    def __init__(self, radius):
        self.radius = radius  # *Property*

    def area(self):  # Implementing *Method*
        return 3.14 * self.radius ** 2

class Rectangle(Shape):  # Another Subclass
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(rectangle.area())
print(circle.area())


# code -5 : Encapsulation
# Encapsulation is one of the core concepts of Object-Oriented Programming (OOP) 
# that is used to restrict direct access to the internal data of a class and only
# allow access through controlled methods.

class Person:
    def __init__(self, name, age, gender):
        self.__name = name  # Private *Property*
        self._age = age     # Protected *Property*
        self.gender = gender # Public *Property*

    # Getter *Method*
    def get_name(self):
        return self.__name

    # Setter *Method*
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name

    # Public *Method*
    def display_info(self):
        print(f"Name: {self.__name}, Age: {self._age}")

person1 = Person("Alice", 30, "Female")
print(person1.gender) # Acessible
# print(person1.name) # Not Accessible
person1.display_info()  # Accessible by public method
person1.set_name("Alicia")
print(person1.get_name())  # Accessible only using getter



# code-6 : Inheritance
# Inheritance allows a class (child class) to acquire properties and methods
#  of another class (parent class).
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Sub-class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Using the inheritance structure:
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())

# code-7: Super keyword
class Animal_:
    def __init__(self, name):
        self.name = name
        print(f"Animal created with name: {self.name}")

class Dog_(Animal_):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        self.breed = breed
        print(f"Dog created with breed: {self.breed}")

d = Dog_("Charlie", "Labrador")


# Code-8: Polymorphism

# Here overridding happens in introduce() method


'''Person defined in Encapsulation'''

#Inherited from Person class 
class Student_(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id  # *Property*

    def introduce(self):  # Unique *Method*
        print(f"I'm {self.get_name()}, a student with ID: {self.student_id}")

#Inherited from Person class
class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject  # *Property*

    def introduce(self):  # Unique *Method*
        print(f"I'm {self.get_name()}, a {self.subject} teacher.")

def person_introduction(obj):  # Common interface
    obj.introduce()

# Create *Objects*
student1 = Student_("Charlie", 20, "Female", "S123")
teacher1 = Teacher("Dave", 45, "Male", "Math")
person_introduction(student1)  # Output: I'm Charlie, a student...
person_introduction(teacher1)  # Output: I'm Dave, a Math teacher...


# Code-9: Method Overloading
class MathOperations:
    # Single method handling multiple cases
    def add(self, a, b, c=0):
        return a + b + c

# Creating object
math_op = MathOperations()

# Calling method with different number of arguments
print(math_op.add(2, 3))
print(math_op.add(2, 3, 4))







