# Multivariate Calculus Notes

---

## Module 1: Fundamentals

### Functions
- A function maps inputs to outputs:  
  \( f: \mathbb{R}^n \rightarrow \mathbb{R} \)
- Example:  
  \( f(x, y) = x^2 + y^2 \)

### Rise Over Run and Derivation
- Derivative represents the rate of change of a function.  
- For a function \( f(x) \), the derivative is:
  $$
  f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
  $$

### Product Rule and Chain Rule
- Product Rule:
  $$
  \frac{d}{dx}[u(x)v(x)] = u'(x)v(x) + u(x)v'(x)
  $$
- Chain Rule:
  $$
  \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
  $$

---

## Module 2: Derivatives and Multivariable Calculus

### Variables, Constants, Context
- Constants remain fixed; variables change.
- When differentiating, treat all other variables as constants unless otherwise specified.

### Jacobian
- The Jacobian matrix represents first-order partial derivatives of vector-valued functions:
  $$
  J = \begin{bmatrix}
  \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
  \vdots & \ddots & \vdots \\
  \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
  \end{bmatrix}
  $$

### Hessian
- The Hessian matrix represents second-order partial derivatives:
  $$
  H = \begin{bmatrix}
  \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots \\
  \frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots \\
  \vdots & \vdots & \ddots
  \end{bmatrix}
  $$

---

## Module 3: Multivariate Chain Rule and Neural Networks

### Multivariate Chain Rule
- If \( z = f(u, v) \), and \( u = g(x, y), v = h(x, y) \), then:
  $$
  \frac{\partial z}{\partial x} = \frac{\partial f}{\partial u} \cdot \frac{\partial g}{\partial x} + \frac{\partial f}{\partial v} \cdot \frac{\partial h}{\partial x}
  $$

### Simple Neural Network
- A single-layer neural network:
  $$
  \hat{y} = \sigma(Wx + b)
  $$
- Where:
  - \( \sigma \): activation function
  - \( W \): weights
  - \( b \): bias

---

## Module 4: Approximation and Series

### Approximate Functions and Taylor Series
- Taylor series expands a function around a point:
  $$
  f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots
  $$

### Power Series and Derivation
- Power series is a generalization of Taylor series:
  $$
  \sum_{n=0}^{\infty} a_n (x - c)^n
  $$

### Linearization and Multivariate Taylor Series
- Linear approximation:
  $$
  f(x, y) \approx f(a, b) + \frac{\partial f}{\partial x}(x-a) + \frac{\partial f}{\partial y}(y-b)
  $$
- Second-order multivariate Taylor:
  $$
  f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a})^T(\mathbf{x} - \mathbf{a}) + \frac{1}{2}(\mathbf{x} - \mathbf{a})^T H_f(\mathbf{a}) (\mathbf{x} - \mathbf{a})
  $$

---

## Module 5: Optimization

### Gradient Descent as Minimization
- Gradient descent updates:
  $$
  \theta = \theta - \eta \nabla f(\theta)
  $$
- Where \( \eta \) is the learning rate.

### Lagrange Multipliers and Constrained Optimization
- To optimize \( f(x, y) \) subject to constraint \( g(x, y) = 0 \), solve:
  $$
  \nabla f = \lambda \nabla g
  $$
- System of equations:
  $$
  \nabla f(x, y) - \lambda \nabla g(x, y) = 0
  $$
  $$
  g(x, y) = 0
  $$

---

## Module 6: Regression

### Simple Linear Regression
- Model:
  $$
  y = mx + c
  $$
- Loss Function (Mean Squared Error):
  $$
  \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
  $$

### Non-Linear Regression (Least Squares)
- General model:
  $$
  y = f(x; \theta) + \epsilon
  $$
- Minimize:
  $$
  \sum_{i=1}^{n} (y_i - f(x_i; \theta))^2
  $$

---

