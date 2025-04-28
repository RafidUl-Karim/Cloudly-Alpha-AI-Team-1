import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
# import class from Oop_master.py
from src.Oop_master import Employee,Example,Student,Circle, Rectangle ,Person,Animal, Dog, Cat,Student_,Teacher,Animal_,Dog_,MathOperations

def test_get_wage():
    # Arrange: Create an Employee object
    emp = Employee(base_salary=30000, overtime=10, rate=20)

    # Act: Call the method
    wage = emp.get_wage()

    # Assert: Check if the result is as expected
    assert wage == 30000 + (10 * 20)  # Expected wage = 30200

'''
means this fixture runs before every test automatically.
Inside, you reset Example.count = 0.

When pytest imports your file to find tests:

It executes top-level code (like print(...), ex = Example(10)).

So your tests start with count = 1, not count = 0.

'''
@pytest.fixture(autouse=True)
def reset_example_count():
    Example.count = 0

def test_example_methods():
    # Create an instance
    ex = Example(10)

    # Test instance method
    assert ex.instance_method() == "Value: 10, Count: 0"

    # Test class method
    output = Example.class_method()
    assert output == "Count updated to: 1"
    assert Example.count == 1  # Confirm that count is really updated

    # Test static method
    assert Example.static_method(3, 4) == 7



def test_init_method():
    
    obj=Student("OudarjaTanmoy",1703002)

    assert obj.name=="OudarjaTanmoy" and obj.roll==1703002

    assert obj.display()==print(f"Name: {obj.name}, Roll: {obj.roll}")


# Test for abstraction
def test_circle_area():
    circle = Circle(5)
    expected_area = 3.14 * 5 ** 2  # 3.14 * 25 = 78.5
    assert circle.area() == expected_area

def test_rectangle_area():
    rectangle = Rectangle(4, 6)
    expected_area = 4 * 6  # 24
    assert rectangle.area() == expected_area

def test_circle_area_zero_radius():
    circle = Circle(0)
    assert circle.area() == 0

def test_rectangle_area_zero_sides():
    rectangle = Rectangle(0, 6)
    assert rectangle.area() == 0
    rectangle2 = Rectangle(4, 0)
    assert rectangle2.area() == 0

# Test for encapsulation
def test_public_property_gender():
    p = Person("Alice", 30, "Female")
    assert p.gender == "Female"

def test_getter_private_name():
    p = Person("Alice", 30, "Female")
    assert p.get_name() == "Alice"

def test_setter_private_name():
    p = Person("Alice", 30, "Female")
    p.set_name("Alicia")
    assert p.get_name() == "Alicia"

def test_set_name_invalid_type():
    p = Person("Alice", 30, "Female")
    p.set_name(12345)  # Passing non-string
    # Name should not change
    assert p.get_name() == "Alice"

def test_display_info(capsys):
    p = Person("Alice", 30, "Female")
    assert p.display_info()==print("Name: Alice, Age: 30")



# Test for inheritance

def test_dog_speak():
    dog = Dog("Buddy")
    assert dog.speak() == "Buddy says Woof!"

def test_cat_speak():
    cat = Cat("Whiskers")
    assert cat.speak() == "Whiskers says Meow!"

def test_animal_speak_not_implemented():
    # Creating a Animal class object named animal
    animal = Animal("Generic Animal")
    # With pytest unimplemented method calling raises issues
    with pytest.raises(NotImplementedError) as exc_info:
        animal.speak()
    
    assert "Subclasses must implement this method." in str(exc_info.value)


# Test for super keyword

def test_animal_initialization(capsys):
    animal = Animal_("Leo")
    captured = capsys.readouterr()
    assert "Animal created with name: Leo" in captured.out
    assert animal.name == "Leo"

def test_dog_initialization(capsys):
    dog = Dog_("Charlie", "Labrador")
    captured = capsys.readouterr()
    # Check both Animal and Dog constructor outputs
    assert "Animal created with name: Charlie" in captured.out
    assert "Dog created with breed: Labrador" in captured.out
    # Also check attributes
    assert dog.name == "Charlie"
    assert dog.breed == "Labrador"


# Test for polymorphism

def teacher_properties():
    obj=Teacher("OudarjaTanmoy",28,"Male","CSE")

    assert obj.get_name()=="OudarjaTanmoy"

    assert obj.age==28
    
    assert obj.gender=="Male"

    assert obj.subject=="CSE"



def student_properties():
    obj=Student_("OudarjaTanmoy",28,"Male",1703002)

    assert obj.get_name()=="OudarjaTanmoy"

    assert obj.age==28
    
    assert obj.gender=="Male"

    assert obj.student_id==1703002


# same method introduce is implemented in 2 different way for 2 object 
def test_teacher_intro():
    obj=Teacher("OudarjaTanmoy",28,"Male","CSE")
    assert obj.introduce()==print(f"I'm {obj.get_name()}, a {obj.subject} teacher.")

def test_student_intro():
    obj=Student_("OudarjaTanmoy",28,"Male",1703002)
    assert obj.introduce()== print(f"I'm {obj.get_name()}, a student with ID: {obj.student_id}")

# Test for method overloading

def test_mathoperation_add():
    math_op=MathOperations()

    math_op.add(2,3)==5
    math_op.add(2,3,5)==10




















