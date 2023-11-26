#!/usr/bin/env python

# Calculating Factorial Recursively:

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    :param n: The number for which to calculate the factorial.
    :return: The factorial of n.
    """
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

result = factorial(5)
print(result)