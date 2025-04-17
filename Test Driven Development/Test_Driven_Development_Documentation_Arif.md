# Software Testing

Testing is the process of evaluating a software application to check:
* It works as expected
* It doesn't have bugs or issues
* It meets user and business requirements

It helps to ensure the quality, reliability, and performance of the software.

# Types of Testing
* Unit testing
* Integration testing
* System testing
* Regression tetsting
* Acceptance testing

# Unit Testing:

Unit testing is a type of software testing where **individual units** or **components** of a program are tested independently to make sure they work as expected.

* A unit can be a **function**, **method**, or **class**.
* It finds **bugs early** in development
* Helps ensure **reliability** and **correctness**
* Tools for unit testing are **unittest, pytest** etc.
* If a function is **add(a, b)** — test if **add(2, 3)** gives **5**.

# Common Assertion Methods in unittest
```python
assertEqual(a, b) – check if a == b
assertNotEqual(a, b) – check if a != b
assertTrue(x) – check if x is True
assertFalse(x) – check if x is False
```
# Integration Testing

Integration testing is a type of software testing where **two or more units/modules** are combined and tested as a group to check if they interact correctly.

* Unit testing checks each function **separately**, while integration testing checks how these functions or compunents work **together**.  
* It finds issues in the **interaction** between components
* Ensures **data flows** correctly from one component to another


## Types of Integration Testing

| Type           | Description |
|----------------|---------------|
| **Big Bang**   | Combine all modules at once and test       |
| **Top-down**   | Start testing from top modules down to lower ones   |
| **Bottom-up**  | Test from lower-level modules (like DB) up to higher modules|
| **Sandwich**   | Mix of top-down and bottom-up                     |


## System Testing

System testing is a type of software testing where the **entire system** (complete application / Completely integrated system) is tested as a whole to ensure it meets all **functional** and **non-functional** requirements.

It tests if the system meets the **specified requirements** and if it is suitable for **delivery** to the end-users. 

### **Tools used for different types os System testing:**

| Type of Testing	| Tools      |
|-----------------|------------|
| Manual Testing	| Test cases, test plans      |
| Automation	    | Selenium, QTP, TestComplete |
| API Testing	    | Postman, REST Assured       |

# Regression Testing
Regression Testing is a type of software testing that ensures new changes (code, features, bug fixes) **do not break existing functionality**.

Regression testing is required whenever we add **new functionalities** or **modify any components** for fixing any bugs or for **improvements**.


# Acceptance Testing

Acceptance Testing is a type of testing done to verify whether the **software meets user needs, requirements, and business processes** and is ready for release.

It is performed from the end-user or client’s perspective to check whether:

* The system works as **expected** in real-world use
* All business **rules and requirements** are met
* the system is ready for **deployment**.




# Unit test Example:
```python
def div(a,b):
    tp_a = type(a)
    tp_b = type(b)
    if (tp_a == int or tp_a == float) and (tp_b == int or tp_b == float):
        if b != 0:
            return a/b
        else:
            return "Divisor can't be 0"
    else:
        return "Invalid data type"
```
## Testing file
```python
import unittest 
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.method import div

class TestMathFunctions(unittest.TestCase):
    def test_add(self): 
        self.assertEqual(div(-150,10), -15) 
        self.assertEqual(div(10,0),"Divisor can't be 0" )
        self.assertEqual(div('5',5), 'Invalid data type')
if __name__ == '__main__':
    unittest.main()
```

# Mocking in Unit Testing
Mocking is a technique used in **unit testing** to replace **real objects, functions, or behaviors** with fake ones (called **mocks**).

* It is used to **avoid calling external systems** (like a database, API, or file system)

**For example**, For testing a function that **sends emails**. we don’t want it to actually send emails during testing. 

So, we can **mock the email service** to pretend it worked and returned “Email sent!”.

## Mock example

```python
# src/greeter.py
import time
def get_current_time():
    return time.ctime()
def greet():
    return f"Hello! It's {get_current_time()}"
```
## Testing Mock
```python
# tests/test_greeter.py
import unittest
from unittest.mock import patch
from src.greeter import greet

class TestGreet(unittest.TestCase):
    @patch('src.greeter.get_current_time', return_value='Monday')
    def test_greet(self, mock_time):
        self.assertEqual(greet(), "Hello! It's Monday")
if __name__ == '__main__':
    unittest.main()
```
We mock **get_current_time()** to always return '**Monday**'.
