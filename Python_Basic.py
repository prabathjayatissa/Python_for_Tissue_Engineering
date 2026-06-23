"""Lession 01"""

def cube(n):
    """Return the cube of n."""
    return n **3
print(cube(3))

def is_even(n):
    """Return True if n is even, otherwise False."""
    return n % 2 == 0
print(is_even(3))

def is_even(n):
    """Check if n is even without using modulus."""
    return (n // 2) * 2 == n
print(is_even(3))

def is_even(n):
    """Check if n is even using bitwise operator."""
    return (n & 1) == 0
print(is_even(3))

def is_even(n):
    """Return True if n is even, otherwise False."""
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(6))

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    f = c * 9/5 + 32
    return f
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

