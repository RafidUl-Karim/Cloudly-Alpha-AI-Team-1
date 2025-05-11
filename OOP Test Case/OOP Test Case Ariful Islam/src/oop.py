# Basic Class and object
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

#######################Super Keword######################
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created with name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        self.breed = breed
        print(f"Dog created with breed: {self.breed}")

######################## Multiple Inheritence ############################

class Father:
    def __init__(self):
        self.father_name = "John"

    def skills(self):
        return ["driving", "fishing"]

class Mother:
    def __init__(self):
        self.mother_name = "Jane"

    def skills(self):
        return ["cooking", "painting"]

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Alex"

    def all_skills(self):
        return Father.skills(self) + Mother.skills(self)


###################### Multilabel Inheritence ##############################

class Grandparent:
    def origin(self):
        print("Grandparent class")

class Parent(Grandparent):
    def middle(self):
        print("Parent class")

class ChildMlt(Parent):
    def last(self):
        print("Child class")

#################### Composition ################################

# Movement behaviors are separate from the Robot class
class Walking:
    def move(self):
        return "I am walking."

class Flying:
    def move(self):
        return "I am flying."

class Robot:
    def __init__(self, movement_behavior):
        self.movement_behavior = movement_behavior  # Composed object

    def move(self):
        return self.movement_behavior.move()

    def set_movement(self, new_movement):
        self.movement_behavior = new_movement  # Change behavior dynamically

###################### Method Overriding ##############################

class PersonOvr:
    def introduce(self):
        return "I am a person."

class Student(PersonOvr):
    def introduce(self):
        return "I am a student. I am learning."

class Teacher(PersonOvr):
    def introduce(self):
        return "I am a teacher. I teach students."

####################### Method Overloading#############################

class MathOperations:
    def add(self, *args):
        print(type(args))
        return sum(args)

#################### Function Decorator ################################

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

# here decorator symbol is used but this task can be done manually
@my_decorator
def say_hello():
    print("Hello!")


##################### Class Deccorator ###############################

# class decorator
def uppercase_decorator(cls):
    class Wrapped(cls):
        def greet(self):
            original = super().greet()
            return original.upper()
    return Wrapped

@uppercase_decorator
class Friend:
    def greet(self):
        return "Hello, friend!"

##################### Property Decorator ###############################

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

####################################################


