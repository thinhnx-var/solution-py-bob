"""
Bob's Mathematical Functions Library

This module provides efficient implementations of common mathematical functions
for use in various computational tasks.
[This is test on MBA]
"""

import math


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: Non-negative integer
        
    Returns:
        n! (n factorial)
        
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: Non-negative integer index
        
    Returns:
        The nth Fibonacci number
        
    Examples:
        >>> fibonacci(10)
        55
        >>> fibonacci(0)
        0
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n: Integer to check for primality
        
    Returns:
        True if n is prime, False otherwise
        
    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(25)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor using Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        The GCD of a and b
        
    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of digits in a non-negative integer.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Sum of all digits in n
        
    Examples:
        >>> sum_of_digits(123)
        6
        >>> sum_of_digits(9876)
        30
    """
    if n < 0:
        raise ValueError("Sum of digits is not defined for negative numbers")
    
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def power(base: float, exponent: int) -> float:
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent (integer)
        
    Returns:
        base^exponent
        
    Examples:
        >>> power(2, 3)
        8.0
        >>> power(5, 0)
        1.0
    """
    if exponent == 0:
        return 1.0
    if exponent < 0:
        return 1.0 / power(base, -exponent)
    
    result = 1.0
    for _ in range(exponent):
        result *= base
    return result


if __name__ == "__main__":
    # Demonstration of the functions
    print("🔢 Bob's Mathematical Functions Demo")
    print("=" * 40)
    
    print(f"factorial(5) = {factorial(5)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"sum_of_digits(123) = {sum_of_digits(123)}")
    print(f"power(2, 3) = {power(2, 3)}")
