# Python Math Functions Solution

Bob's implementation of various mathematical functions in Python.

## Functions Implemented

- `factorial(n)` - Calculate factorial of a number
- `fibonacci(n)` - Calculate nth Fibonacci number  
- `is_prime(n)` - Check if a number is prime
- `gcd(a, b)` - Calculate greatest common divisor
- `sum_of_digits(n)` - Calculate sum of digits in a number
- `lcm(a, b)` - Calculate least common multiple
- `is_perfect_square(n)` - Check if a number is a perfect square

## Installation

### Using Poetry (Recommended)

```bash
# Install dependencies
poetry install

# Activate the virtual environment
poetry shell

# Or run commands directly
poetry run python src/math_functions.py
```

### Using pip

```bash
# Install in development mode
pip install -e .

# Or install requirements
pip install -r requirements.txt
```

## Build and Test

```bash
# With Poetry
poetry run python src/math_functions.py

# Run tests (when Alice's test suite is merged)
poetry run pytest

# Without Poetry
python src/math_functions.py
pytest
```

## Usage

```python
from src import factorial, fibonacci, is_prime, gcd, sum_of_digits

# Calculate factorial
fact = factorial(5)  # 120

# Get Fibonacci number
fib = fibonacci(10)  # 55

# Check if prime
prime = is_prime(17)  # True

# Calculate GCD
gcd_result = gcd(48, 18)  # 6

# Sum digits
digit_sum = sum_of_digits(123)  # 6
```

## Project Structure

```
solution-py-bob/
├── src/
│   ├── __init__.py
│   └── math_functions.py
├── pyproject.toml
├── requirements.txt
└── README.md
```
