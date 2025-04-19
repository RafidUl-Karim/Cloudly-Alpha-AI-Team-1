###  Python Testing Theory & Mocking Explained


###  What is Software Testing?

**Software testing** is the process of evaluating a software application to ensure it meets the expected requirements and is free of bugs. The goal is to identify defects early, ensure reliability, and maintain code quality.

---

###  Types of Testing in Python

#### 1. **Unit Testing**
- **Definition**: Testing individual components or functions in isolation.
- **Goal**: Ensure each unit performs as expected.
- **Tool**: `unittest`, `pytest`

```python
# Math_util.py
def add(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        return "Both arguments must be numbers"
        # raise TypeError("Both arguments must be numbers")
    return a + b

# Test_math_utils/test.py

import unittest
import sys
import os

# Add the parent directory to the Python path
# It dynamically figures out the correct path based on where the test
# file is, and it's robust across environments.
# This line is used to add the parent directory of the current file to
# Python's import search path, so that you can import your module even 
# if it’s in a different folder.

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Math_util import add
class TestMathUtils(unittest.TestCase):

    # test for Add
    def test_add_valid(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_invalid(self):
        self.assertEqual(add("2", 3), "Both arguments must be numbers")


if __name__ == '__main__':
    unittest.main()

```

---

#### 2. **Integration Testing**
- **Definition**: Testing the interaction between multiple modules or components.
- **Goal**: Verify combined parts work together correctly.

---

#### 3. **System Testing**
- **Definition**: Testing the entire system as a whole.
- **Goal**: Validate the complete and integrated software against requirements.

---

#### 4. **Acceptance Testing**
- **Definition**: Testing to determine whether the system meets business requirements and is ready for delivery.
- **Usually performed by**: End users or stakeholders.

---

#### 5. **Regression Testing**
- **Definition**: Re-running tests after code changes to ensure existing functionality still works.
- **Goal**: Prevent new bugs in previously working areas.

---

#### 6. **Smoke Testing**
- **Definition**: A basic test to check the core functionality of an application.
- **Goal**: Ensure the application is stable enough for deeper testing.

---

#### 7. **Performance Testing**
- **Definition**: Evaluating how the system performs under load or stress.
- **Types**: Load testing, stress testing, scalability testing.

---

#### Testing Tools in Python

| Tool         | Purpose                        |
|--------------|--------------------------------|
| `unittest`   | Built-in testing framework     |
| `pytest`     | More advanced and flexible     |
| `doctest`    | Tests in documentation strings |
| `mock`       | Mocks external dependencies    |
| `coverage`   | Measures test coverage         |

---

#### What is Mocking?

##### Definition:
**Mocking** is a technique used in testing where real objects or functions are replaced with fake ones (mocks) that simulate the behavior of the real ones.

#### Why Mock?
- To isolate the code under test  
- To avoid slow, unreliable, or unavailable external systems (like databases, APIs)  
- To return controlled, predictable values for testing  
- To verify that certain functions are called with the right arguments  

---

#### Example of Mocking in Python

Suppose you want to test a function that makes an HTTP request:


```python
# api_client.py
import requests

def fetch_data():
    response = requests.get("https://example.com")
    return response.json()


# test_api_client.py
import unittest
from unittest.mock import patch
from api_client import fetch_data

class TestAPI(unittest.TestCase):

    @patch('api_client.requests.get')
    def test_fetch_data(self, mock_get):
        # Configure the mock to return custom data
        mock_get.return_value.json.return_value = {"message": "ok"}

        # Call the function under test
        result = fetch_data()

        # Assert that the function behaves correctly
        self.assertEqual(result, {"message": "ok"})

if __name__ == '__main__':
    unittest.main()
```
---

#### Unit Testing in Machine Learning Using Seed

In machine learning, **unit tests ensure the correctness** of individual components like data preprocessing, model training, and prediction. However, **randomness** (e.g., in data splitting or weight initialization) can cause **non-deterministic behavior**. Using a **fixed seed** allows us to test ML code **consistently and reliably**.

---

- Ensures **reproducibility**
- Avoids **flaky tests** (that randomly pass or     fail)
- Allows **debugging** based on consistent outputs

---
##### Example:
```python

# model_trainer.py

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def train_and_evaluate(X, y, seed=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_pred)



### test/test_model_trainer.py

import numpy as np
from model_trainer import train_and_evaluate

def test_train_and_evaluate_deterministic():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    y = np.random.rand(100)

    score1 = train_and_evaluate(X, y, seed=42)
    score2 = train_and_evaluate(X, y, seed=42)

    assert score1 == score2, "Results should be deterministic when using the same seed"
```

