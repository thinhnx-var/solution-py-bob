# Make src directory a package
from .math_functions import (
    factorial,
    fibonacci, 
    is_prime,
    gcd,
    sum_of_digits,
    lcm,
    is_perfect_square
)

__all__ = [
    'factorial',
    'fibonacci', 
    'is_prime',
    'gcd', 
    'sum_of_digits',
    'lcm',
    'is_perfect_square'
]
