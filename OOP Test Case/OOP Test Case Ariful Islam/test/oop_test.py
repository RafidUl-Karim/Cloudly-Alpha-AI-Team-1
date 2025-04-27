# tests/test_person.py

from oop import Person, Dog, Child, ChildMlt, Walking, Flying, Robot, Student, Teacher, MathOperations, say_hello, Friend, Circle

def test_class_object():
    p = Person("Salsabil", 20)
    assert p.name == "Salsabil"
    assert p.age == 20

def test_super_keword():
    dog = Dog("Charlie", "Labrador")
    assert dog.name == "Charlie"
    assert dog.breed == "Labrador"

def test_multiple_inheritance():
    c = Child()
    assert c.father_name == "John"
    assert c.mother_name == "Jane"
    assert c.child_name == "Alex"
    assert set(c.all_skills()) == {"driving", "fishing", "cooking", "painting"}

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

def test_composition():
    walker = Walking()
    flyer = Flying()

    robot = Robot(walker)
    assert robot.move() == "I am walking."

    robot.set_movement(flyer)
    assert robot.move() == "I am flying."

def test_method_overriding():
    student = Student()
    teacher = Teacher()

    # Check overridden methods
    assert student.introduce() == "I am a student. I am learning."
    assert teacher.introduce() == "I am a teacher. I teach students."


def test_overloading():
    math_ops = MathOperations()

    # Test case for addition with multiple numbers
    result = math_ops.add(1, 2, 3, 4)
    assert result == 10  # 1 + 2 + 3 + 4 = 10

    # Test case for no arguments
    result = math_ops.add()
    assert result == 0  # No numbers, so result should be 0

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