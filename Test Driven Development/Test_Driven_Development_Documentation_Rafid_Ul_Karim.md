# Python Testing Overview

A practical guide to different types of testing in Python. Includes examples, how to run tests, and tips relevant to ML workflows.

---

## Unit Testing

Unit tests validate the behavior of individual units of code (usually functions or methods).  They help catch bugs early and promote modular, testable design.

### Example using `unittest` (with `main`)


```python
import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)"

# This allows the script to be run directly
if __name__ == '__main__':
    unittest.main()
```
### Example using `pytest` (no `main` needed)
```python
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 4) == 8
```

### **Runing Unit Tests:**

#### Running Unit Test files directly:
To run unit test files directly we must ensure to add: 
```python
if __name__ ==  '__main__': 
	unittest.main()
```

#### From Command Prompt using `pytest`:
`pytest paht/to/test_multiply.py`

#### From Command Prompt using `unittest`:
`python -m unittest path/to/test_file.py`

### Common Assertions
A list of frequently used assertions in unit testing
```python
self.assertEqual(a, b)         # a == b
self.assertNotEqual(a, b)      # a != b
self.assertTrue(condition)     # condition is True
self.assertFalse(condition)    # condition is False
self.assertIsNone(value)       # value is None
self.assertIsNotNone(value)    # value is not None

```

---

## Integration Testing

Integration tests verify that multiple components or modules work correctly when combined.  

**For example:** Ensuring that a database, API, and service layer interact as expected.  Typically written after individual units have been tested in isolation.

**Use Case:** We are building an e-commerce app.
- We want to test whether the order placement process correctly interacts with the payment gateway, inventory system, and email confirmation service.

---

## System Testing

System tests validate the entire application as a complete system.  They simulate end-to-end workflows and mimic real user interactions.  
Often conducted in environments close to production.

**Use Case:** Before releasing a mobile banking app, the QA team tests the following flow on multiple devices and OS versions to ensure everything works as expected end-to-end: `full login → account view → fund transfer → logout`

---

## Regression Testing

Regression tests ensure that recent changes haven't broken existing features.  They are especially useful when refactoring or adding new functionality.  Usually automated and executed continuously (CI/CD pipelines).

**Use Case:** We fix a bug in a machine learning model’s feature normalization step.
- After deploying the fix, we re-run the full test suite to confirm that other parts of the data pipeline (e.g., training loop, evaluation metrics) still behave correctly.

---

## Acceptance Testing

Acceptance tests check whether the system meets business requirements and stakeholder expectations.  Typically written based on user stories or specifications.  Often performed by QA teams or end-users.

**Use Case:** A client asks for a web form to collect user feedback.
- Acceptance criteria might include: "form must not submit if email is empty" and "a thank you message must be shown after submission."
- By demoing the working form, the client can sign off on delivery.

---

## Using `@mock` in Tests

Mocking replaces parts of the system with controlled stand-ins during testing.  This isolates the code under test and removes dependency on external systems (e.g., APIs, DBs).

**Use Case:** A ML training script pulls real-time stock data using an API.
- In unit tests, we can use `@mock` to simulate API responses to avoid network calls, speed up tests, and make outcomes predictable:


### Example using `unittest.mock`
```python
from unittest.mock import patch

@patch('module.fetch_data')
def test_mocked_fetch(mock_fetch):
    mock_fetch.return_value = {'price': 100}
    result = some_function()
    assert result == expected_output

```
-   `patch()` replaces the real `fetch_data` during the test.
    
-   Helps make tests faster, more reliable, and deterministic.
---

## Setting Seed Values in ML Testing

Machine Learning models often include randomness in training.  To ensure reproducibility during tests, always set random seeds.

**Use Case:** Writing a test to check if a model improves after a training step.
- Without a fixed seed, weight initialization and data shuffling may cause test results to vary.
- This leads to flaky tests that pass or fail unpredictably.

### Example:
```python
import numpy as np
import tensorflow as tf
import random

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

```
By calling `set_seed()` in the test setup, we can ensure the that results are consistent across test runs and environments. 

---

