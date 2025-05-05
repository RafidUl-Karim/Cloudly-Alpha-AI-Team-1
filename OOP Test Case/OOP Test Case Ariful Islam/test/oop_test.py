# tests/test_person.py
import pytest
from oop import Person, Dog, Child, ChildMlt, Walking, Flying, Robot, Student, Teacher, MathOperations, say_hello, Friend, Circle, PersonOvr

def test_class_object():
    p = Person("Salsabil", 20)
    assert p.name == "Salsabil"
    assert p.age == 20
    assert p.name.isalpha(), f"{p.name} should be a Alphabets"

def test_super_keword():
    dog = Dog("Charlie", "Labrador")
    assert dog.name == "Charlie"
    assert dog.breed == "Labrador"

@pytest.fixture 
def child():
    return Child()

@pytest.mark.parametrize("name", ["father_name", "mother_name", "child_name"])
def test_name_is_string_and_minlength_2(child, name):
    value = getattr(child, name)
    assert isinstance(value, str), f"{name} should be a string"
    assert value.isalpha(), f"{name} should be a Alphabets"
    assert len(value) >= 2, f"{name} should have at least 2 characters"

def test_multilabe_inheritance(capfd):
    c = ChildMlt()  # create Child object

    # Call inherited and own methods
    c.origin()   # from Grandparent
    c.middle()   # from Parent
    c.last()     # from Child

    # Capture printed output using pytest's capfd fixture
    out, _ = capfd.readouterr()

    # Check if expected strings are in the output
    assert "Grandparent class" in out
    assert "Parent class" in out
    assert "Child class" in out

# Testing composition
@pytest.mark.parametrize("behavior,expected", [
    (Walking(), "I am walking."),
    (Flying(), "I am flying.")
])
def test_robot_movement_parameterized(behavior, expected):
    robot = Robot(behavior)
    assert robot.move() == expected

def test_invalid_movement_object():
    class InvalidMovement:
        pass  # No move method

    robot = Robot(Walking())
    robot.set_movement(InvalidMovement())

    with pytest.raises(AttributeError):
        robot.move()

# Testing Overriding
@pytest.mark.parametrize("obj, expected", [
    (PersonOvr(), "I am a person."),
    (Student(), "I am a student. I am learning."),
    (Teacher(), "I am a teacher. I teach students.")
])
def test_parametrized_introductions(obj, expected):
    assert obj.introduce() == expected

def test_instance_types():
    assert isinstance(Student(), PersonOvr)
    assert isinstance(Teacher(), PersonOvr)
    assert not isinstance(PersonOvr(), Student)

# Overloading test
@pytest.fixture
def math():
    return MathOperations()
def test_add_raises_typeerror_on_invalid_type(math):
    with pytest.raises(TypeError):
        math.add(1, '2', 3)  # can't sum int and str

def test_args_is_tuple(math, capsys):
    math.add(1, 2)
    captured = capsys.readouterr()
    assert "<class 'tuple'>" in captured.out

def test_overloading():
    math_ops = MathOperations()

    # Test case for addition with multiple numbers
    result = math_ops.add(1, 2, 3, 4)
    assert result == 10  # 1 + 2 + 3 + 4 = 10

    # Test case for no arguments
    result = math_ops.add()
    assert result == 0  # No numbers, so result should be 0


# testing decorator
def test_decorator(capfd):
    say_hello()
    out, err = capfd.readouterr()
    assert out == "Before the function runs\nHello!\nAfter the function runs\n"

def test_class_decorator():
    p = Friend()
    assert p.greet() == "HELLO, FRIEND!"

def test_property_decorator():
    c = Circle(5)
    assert c.diameter == 10
def test_diameter_is_read_only():
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.diameter = 10  # Trying to set a read-only @property